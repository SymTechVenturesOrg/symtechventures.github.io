from __future__ import annotations
import hashlib
from io import BytesIO
import json
import re
import subprocess
import threading
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
from PIL import Image, ImageStat
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "phase3-p2-browser-qa-artifacts"
OUT.mkdir(parents=True, exist_ok=True)
PREP = json.loads((ROOT / "docs/reports/V2_PHASE_03_P2_SEVEN_RESPONSIVE_IMAGE_INTEGRATION_PREPARATION_MANIFEST_20261121.json").read_text())
MEASURED = json.loads((ROOT / "docs/reports/V2_PHASE_03_P2_SEVEN_RESPONSIVE_WEBP_DERIVATIVE_MANIFEST_20261121.json").read_text())
ARTICLE = "/articles/symmetria/symmetria-paper-02.html"
CASES = (
    ("mobile-320-dpr1", 320, 740, 1, True),
    ("mobile-390-dpr1", 390, 844, 1, True),
    ("mobile-390-dpr2", 390, 844, 2, True),
    ("tablet-768-dpr1", 768, 1024, 1, True),
    ("desktop-1440-dpr1", 1440, 900, 1, False),
    ("desktop-1440-dpr2", 1440, 900, 2, False),
)
issues: list[str] = []
results: list[dict] = []
SLOTS = [x["figure_slot_attr"] for x in PREP["images"]]

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        return

def check(ok: bool, message: str) -> None:
    if not ok:
        issues.append(message)

def binary_preflight() -> dict:
    records=[]
    for item in MEASURED["images"]:
        p=ROOT/item["master_path"]
        data=p.read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        blob=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
        im=Image.open(p); im.verify(); im=Image.open(p); im.load()
        check(digest==item["source_sha256"], item["slot"]+": copied PNG SHA-256 mismatch")
        check(len(data)==item["source_bytes"], item["slot"]+": copied PNG size mismatch")
        check(blob==item["source_git_blob_sha"], item["slot"]+": PNG Git blob differs from approved source")
        check(im.format=="PNG" and im.mode=="RGB" and im.size==(1920,1080),item["slot"]+": invalid master PNG decode/dimensions")
        records.append({"slot":item["slot"],"path":item["master_path"],"bytes":len(data),"sha256":digest,"git_blob_sha":blob,"format":im.format,"mode":im.mode,"dimensions":list(im.size)})
        for v in item["variants"]:
            q=ROOT/v["path"]; raw=q.read_bytes(); webp=Image.open(q); webp.verify(); webp=Image.open(q); webp.load()
            check(hashlib.sha256(raw).hexdigest()==v["sha256"],item["slot"]+f" {v['width']}w: WebP SHA-256 mismatch")
            check(len(raw)==v["bytes"],item["slot"]+f" {v['width']}w: WebP size mismatch")
            check(webp.format=="WEBP" and webp.mode=="RGB" and webp.size==(v["width"],v["height"]),item["slot"]+f" {v['width']}w: WebP decode/geometry mismatch")
            check(v["master_sha256"]==digest,item["slot"]+f" {v['width']}w: wrong source-master association")
    check(sum(x["bytes"] for x in records)==22023720,"approved source total differs from 22,023,720 bytes")
    return {"approved_master_pngs":records,"master_count":len(records),"webp_count":sum(len(x["variants"]) for x in MEASURED["images"])}

def browser_case(browser, origin, name, width, height, dpr, touch):
    context=browser.new_context(viewport={"width":width,"height":height},device_scale_factor=dpr,has_touch=touch,is_mobile=touch,reduced_motion="reduce")
    context.route("**/*",lambda route: route.continue_() if route.request.url.startswith(origin+"/") else route.abort())
    page=context.new_page(); errors=[]; external=[]; failed=[]
    page.on("pageerror",lambda e:errors.append(str(e)))
    page.on("console",lambda m:errors.append(m.text) if m.type=="error" else None)
    page.on("requestfailed",lambda r:failed.append({"url":r.url,"failure":r.failure}))
    page.on("request",lambda r:external.append(r.url) if not r.url.startswith(origin+"/") else None)
    record={"name":name,"viewport":[width,height],"dpr":dpr,"touch_emulation":touch,"figures":[],"screenshots":[]}
    try:
        response=page.goto(origin+ARTICLE,wait_until="domcontentloaded",timeout=30000)
        check(response is not None and response.status==200,name+": article HTTP response not 200")
        count=page.locator("figure.paper-figure--cinematic").count()
        check(count==7,name+f": expected 7 figures, got {count}")
        order=page.locator("figure.paper-figure--cinematic").evaluate_all("els=>els.map(e=>e.dataset.figureSlot)")
        check(order==SLOTS,name+": figure order/slot mismatch")
        active_navigation=page.evaluate("""()=>Object.fromEntries(['.site-header .main-nav','.site-header .mobile-list'].map(sel=>[sel,Array.from(document.querySelectorAll(sel+' [aria-current="page"]')).map(a=>({text:a.textContent.trim(),href:a.getAttribute('href')}))]))""")
        record["active_navigation"]=active_navigation
        for nav,active in active_navigation.items():
            check(len(active)==1 and active[0]["text"]=="Discussion Papers" and active[0]["href"]=="../../pages/discussion-series.html",name+f": incorrect or duplicate aria-current page in {nav}")
        dimensions=page.evaluate("()=>({client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth})")
        record["document_dimensions"]=dimensions
        check(dimensions["scroll"]<=dimensions["client"]+1,name+": horizontal overflow")
        if width in (320,390):
            menu=page.locator(".site-header .mobile-nav summary")
            header_rects=page.evaluate("""()=>{const menu=document.querySelector('.site-header .mobile-nav summary').getBoundingClientRect(),brand=document.querySelector('.site-header .brand').getBoundingClientRect();return {menuLeft:menu.left,menuRight:menu.right,brandRight:brand.right,viewport:document.documentElement.clientWidth}}""")
            record["mobile_header"]=header_rects
            check(header_rects["menuLeft"]>=0 and header_rects["menuRight"]<=width-1,name+": mobile menu button clipped by viewport")
            check(header_rects["brandRight"]<=header_rects["menuLeft"]+1,name+": brand overlaps mobile menu")
            menu.click()
            drawer=page.locator(".site-header .mobile-nav[open] .mobile-list")
            links=drawer.locator("a")
            drawer_rect=drawer.bounding_box()
            record["mobile_menu_open"]={"link_count":links.count(),"drawer_rect":drawer_rect}
            check(drawer.is_visible() and links.count()==6 and all(links.nth(i).is_visible() for i in range(links.count())),name+": mobile menu links missing or invisible")
            check(drawer_rect is not None and drawer_rect["x"]>=-1 and drawer_rect["x"]+drawer_rect["width"]<=width+1,name+": mobile navigation drawer clipped")
            if dpr==1:
                dest=OUT/(name+"-mobile-menu-open.png")
                page.screenshot(path=str(dest),full_page=False,animations="disabled")
                record["screenshots"].append(dest.name)
            menu.click()

        if name in ("mobile-320-dpr1","mobile-390-dpr1","tablet-768-dpr1","desktop-1440-dpr1"):
            record["screenshots"].append("page-top.png")
            page.screenshot(path=str(OUT/(name+"-page-top.png")),full_page=False,animations="disabled")
        for item in PREP["images"]:
            slot=item["figure_slot_attr"]; selector=f'figure[data-figure-slot="{slot}"]'; fig=page.locator(selector)
            check(fig.count()==1,name+f": missing/duplicate {slot}")
            if fig.count()!=1: continue
            fig.scroll_into_view_if_needed(timeout=15000)
            page.wait_for_function("sel=>{const i=document.querySelector(sel+' img');return !!i&&i.complete&&i.naturalWidth>0}",arg=selector,timeout=20000)
            page.locator(selector+" img").evaluate("img=>img.decode()")
            page.evaluate("()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))")
            inf=fig.evaluate("""f=>{const i=f.querySelector('img'),a=f.querySelector('a.paper-figure-open'),c=f.querySelector('figcaption'),d=f.querySelector('.figure-description'),r=i.getBoundingClientRect();return {slot:f.dataset.figureSlot,src:i.currentSrc,srcWidth:Number((i.currentSrc.match(/_(\\d+)w_q93\\.webp/)||[])[1]||0),renderedWidth:r.width,renderedHeight:r.height,naturalWidth:i.naturalWidth,naturalHeight:i.naturalHeight,alt:i.alt,describedBy:i.getAttribute('aria-describedby'),descriptionId:d?.id,description:d?.textContent.trim(),caption:c?.textContent.trim(),captionVisible:!!c&&c.getBoundingClientRect().width>0,descriptionVisible:!!d&&d.getBoundingClientRect().width>0,captionTextAlign:getComputedStyle(c).textAlign,captionFontSizePx:parseFloat(getComputedStyle(c).fontSize),captionLineHeightPx:parseFloat(getComputedStyle(c).lineHeight),descriptionTextAlign:getComputedStyle(d).textAlign,href:a.href,ariaLabel:a.getAttribute('aria-label'),target:a.target,rel:a.rel,loading:i.loading,fetchpriority:i.fetchPriority,sizes:i.sizes}}""")
            if width in (320,390) and dpr==1:
                paint_stddev=0.0
                paint_attempts=0
                for attempt in range(1,4):
                    img_bytes=page.locator(selector+" img").screenshot(animations="disabled")
                    sample=Image.open(BytesIO(img_bytes)).convert("L")
                    w,h=sample.size
                    sample=sample.crop((int(.08*w),int(.08*h),int(.92*w),int(.92*h)))
                    paint_stddev=round(ImageStat.Stat(sample).stddev[0],2)
                    paint_attempts=attempt
                    if paint_stddev>=14: break
                    page.wait_for_timeout(250)
                inf["paint_stddev_luma"]=paint_stddev
                inf["paint_attempts"]=paint_attempts
                check(paint_stddev>=14,name+f" {slot}: image loaded but did not visibly paint in mobile screenshot")
            record["figures"].append(inf)
            check(inf["naturalWidth"]>0 and inf["naturalHeight"]>0,name+f" {slot}: selected responsive image failed to decode")
            check(inf["srcWidth"] in (768,1280,1920) and inf["srcWidth"]+1>=inf["renderedWidth"]*dpr*.95,name+f" {slot}: responsive candidate undersized or unlisted")
            check(inf["alt"]==item["img_alt"],name+f" {slot}: alt differs from approved text")
            check(inf["caption"]==item["figcaption_proposed"],name+f" {slot}: caption differs from qualified manifest text")
            check(inf["description"]==item["description_proposed"],name+f" {slot}: accessible description differs from manifest")
            check(inf["describedBy"]==inf["descriptionId"] and inf["descriptionVisible"],name+f" {slot}: missing visible aria-describedby target")
            check(inf["captionVisible"],name+f" {slot}: visible caption missing")
            if width in (320,390):
                check(inf["captionTextAlign"]=="left",name+f" {slot}: mobile figure caption is not left-aligned")
                check(inf["descriptionTextAlign"]=="left",name+f" {slot}: mobile figure description is not left-aligned")
                check(inf["captionFontSizePx"]>=15 and inf["captionLineHeightPx"]>=24,name+f" {slot}: mobile caption font size or line height is below the readability threshold")
            check(inf["href"].endswith(item["site_master_png"]),name+f" {slot}: full-resolution PNG link wrong")
            check(inf["target"]=="_blank" and "noopener" in inf["rel"] and "full-resolution" in inf["ariaLabel"].lower(),name+f" {slot}: secure/accessibly named new-tab PNG link missing")
            check(abs(inf["renderedWidth"]/inf["renderedHeight"]-16/9)<.025,name+f" {slot}: displayed ratio is not 16:9")
            check(inf["loading"]==("eager" if slot=="cover" else "lazy"),name+f" {slot}: wrong loading policy")
            if slot=="cover": check(inf["fetchpriority"]=="high",name+": cover fetch priority is not high")
            if slot=="figure-1-1": check("approximate balance" in inf["caption"] and "precise invariance" in inf["caption"] and "different mechanisms" in inf["description"],name+": natural approximation versus ideal invariance qualification absent")
            if slot=="figure-2-1": check("exact golden-ratio" in inf["caption"] and "No golden rectangle" in inf["description"],name+": Figure 2.1 no-exact-fit qualification absent")
            if slot=="figure-3-1": check("not translational invariance" in inf["caption"] and "not invariant at its original position" in inf["description"],name+": translation qualification absent")
            if slot=="figure-4-1": check("no net external torque" in inf["caption"],name+": Noether conditions absent")
            if slot=="figure-5-1": check("one-dimensional" in inf["caption"] and "not a complete Mexican-hat" in inf["caption"],name+": potential-model qualification absent")
            if slot=="figure-6-1": check("untested hypothesis" in inf["caption"].lower() and "not established physics" in inf["description"].lower(),name+": exploratory/unestablished caveat absent")
            if width in (320,390) and slot in ("figure-2-1","figure-3-1","figure-6-1") and dpr==1:
                record["screenshots"].append(slot+"-figure.png")
                page.screenshot(path=str(OUT/(name+"-"+slot+".png")),full_page=False,animations="disabled")
        page.wait_for_timeout(200)
        resources=page.evaluate("""()=>performance.getEntriesByType('resource').filter(e=>e.name.includes('/images/symmetria/paper-02/approved-20261121/')&&e.name.endsWith('.webp')).map(e=>({url:e.name,transferBytes:e.transferSize,encodedBodyBytes:e.encodedBodySize,decodedBodyBytes:e.decodedBodySize}))""")
        expected={f["src"] for f in record["figures"]}; selected=[x for x in resources if x["url"] in expected]
        record["webp_network"]=selected
        record["webp_selected_body_bytes"]=sum(x["encodedBodyBytes"] for x in selected)
        record["webp_transfer_bytes"]=sum(x["transferBytes"] for x in selected)
        check(len({x["url"] for x in selected})==7,name+": browser resource timing did not observe seven chosen WebPs")
        check(all(x["encodedBodyBytes"]>0 for x in selected),name+": browser returned zero WebP body size")
        for f in record["figures"]:
            a=page.locator(f'figure[data-figure-slot="{f["slot"]}"] a.paper-figure-open')
            if name=="desktop-1440-dpr1":
                a.focus()
                with page.expect_popup(timeout=15000) as pop:
                    page.keyboard.press("Enter")
                pp=pop.value; pp.wait_for_load_state("load",timeout=20000); image=pp.locator("img").evaluate("i=>({complete:i.complete,width:i.naturalWidth,height:i.naturalHeight})")
                check(image["width"]==1920 and image["height"]==1080,name+f" {f['slot']}: PNG full resolution failed")
                pp.close()
        if name=="mobile-390-dpr1":
            got=False
            for _ in range(50):
                page.keyboard.press("Tab")
                if page.evaluate("document.activeElement?.matches('figure[data-figure-slot=cover] a.paper-figure-open')"):
                    got=True;break
            record["tab_reaches_cover_link"]=got
            record["cover_keyboard_focus_visible"]=page.locator('figure[data-figure-slot="cover"] a.paper-figure-open').evaluate("e=>e.matches(':focus-visible')") if got else False
            check(record["tab_reaches_cover_link"] and record["cover_keyboard_focus_visible"],name+": keyboard focus doesn't reach visible cover link")
        record["page_errors"]=errors; record["failed_requests"]=failed;record["external_requests_blocked"]=external
        check(not errors,name+": JavaScript/console errors "+repr(errors[:4]))
        check(not external,name+": unexpected external requests "+repr(external[:4]))
    except Exception as exc:
        record["exception"]=str(exc);issues.append(name+": browser exception "+str(exc))
    finally:
        results.append(record);context.close()

def broken_image_case(browser,origin):
    ctx=browser.new_context(viewport={"width":320,"height":740},device_scale_factor=1,is_mobile=True,has_touch=True)
    ctx.route("**/*",lambda route:route.continue_() if route.request.url.startswith(origin+"/") else route.abort())
    ctx.route("**/p2_figure_2_1_768w_q93.webp",lambda route:route.abort())
    page=ctx.new_page(); record={"name":"deliberate-block-figure-2-1"}
    try:
        page.goto(origin+ARTICLE,wait_until="domcontentloaded",timeout=30000); fig=page.locator('figure[data-figure-slot="figure-2-1"]');fig.scroll_into_view_if_needed()
        page.wait_for_function("()=>{const i=document.querySelector('figure[data-figure-slot=figure-2-1] img');return !!i&&i.complete}",timeout=15000)
        record.update(fig.evaluate("f=>{const i=f.querySelector('img'),c=f.querySelector('figcaption'),d=f.querySelector('.figure-description');return {broken:i.naturalWidth===0,alt:i.alt,captionVisible:!!c&&c.getBoundingClientRect().width>0,descriptionVisible:!!d&&d.getBoundingClientRect().width>0,linkToMaster:f.querySelector('a.paper-figure-open').href}}") )
        check(record["broken"] and record["alt"] and record["captionVisible"] and record["descriptionVisible"],"blocked image: useful text fallback absent")
        check(record["linkToMaster"].endswith("p2_figure_2_1_master_1920x1080.png"),"blocked image: master link absent")
        dest=OUT/"deliberate-block-figure-2-1.png";page.screenshot(path=str(dest),full_page=False);record["screenshot"]=dest.name
    except Exception as exc: record["exception"]=str(exc);issues.append("blocked-image case: "+str(exc))
    finally:results.append(record);ctx.close()

def main():
    binary=binary_preflight()
    server=ThreadingHTTPServer(("127.0.0.1",0),partial(QuietHandler,directory=str(ROOT)))
    thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();origin=f"http://127.0.0.1:{server.server_port}"
    try:
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True,args=["--no-sandbox"])
            try:
                for case in CASES: browser_case(browser,origin,*case)
                broken_image_case(browser,origin)
            finally:browser.close()
    except Exception as exc:issues.append("fatal Chromium startup/browser failure: "+str(exc))
    finally:server.shutdown();server.server_close()
    out={"generated_utc":datetime.now(timezone.utc).isoformat(),"git_commit":subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip(),"browser":"Chromium via Playwright on GitHub Actions ubuntu-24.04","article":ARTICLE,"binary_preflight":binary,"acceptance_status":"PASS" if not issues else "FAIL","cases":results,"issues":issues,"physical_handset_or_screen_reader_tested":False,"notes":["DPR is browser emulation; not a physical device.","Figure artwork includes fine scientific text. At phone display widths, image microcopy is not relied upon; HTML captions/descriptions remain visible and full-resolution original PNGs open in a new tab.","Encoded body/transfer bytes are Playwright same-origin browser resource-timing measurements, not a cellular-network performance guarantee.","The deliberately blocked derivative verifies that the image alt, visible caption, long description and master-PNG link remain present."]}
    (OUT/"browser-acceptance.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n")
    for c in results:
        if "webp_selected_body_bytes" in c:print("BROWSER_CASE "+json.dumps({"name":c["name"],"viewport":c["viewport"],"dpr":c["dpr"],"selected_widths":[i["srcWidth"] for i in c["figures"]],"webp_body_bytes":c["webp_selected_body_bytes"],"webp_transfer_bytes":c["webp_transfer_bytes"],"overflow":c["document_dimensions"],"errors":c["page_errors"],"external_requests":c["external_requests_blocked"]}))
    print("ACCEPTANCE "+out["acceptance_status"]+" issues="+json.dumps(issues))
    raise SystemExit(0 if not issues else 1)
if __name__=="__main__":main()

