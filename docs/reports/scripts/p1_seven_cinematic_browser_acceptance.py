"""GitHub-native, non-deploying Playwright acceptance for Paper One's 7 compressed figures."""
from __future__ import annotations

import json
import subprocess
import sys
import threading
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "phase3-p1-browser-qa-artifacts"
OUTPUT.mkdir(parents=True, exist_ok=True)
ROUTE = "/articles/symmetria/symmetria-paper-01.html"
SLOTS = ("cover", "figure-1-1", "figure-2-1", "figure-3-1", "figure-4-1", "figure-5-1", "figure-6-1")
CASES = (
    ("mobile-320-dpr1", 320, 740, 1, True),
    ("mobile-390-dpr1", 390, 844, 1, True),
    ("mobile-390-dpr2", 390, 844, 2, True),
    ("tablet-768-dpr1", 768, 1024, 1, True),
    ("desktop-1440-dpr1", 1440, 900, 1, False),
    ("desktop-1440-dpr2", 1440, 900, 2, False),
)
issues = []
results = []


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        return


def check(condition, label):
    if not condition:
        issues.append(label)


def safe_screenshot(page, label, selector=None):
    try:
        dest = OUTPUT / (label + ".png")
        if selector:
            page.locator(selector).screenshot(path=str(dest), timeout=15000)
        else:
            page.screenshot(path=str(dest), full_page=False, timeout=15000)
        return str(dest.relative_to(ROOT))
    except Exception as exc:
        issues.append("screenshot " + label + ": " + str(exc))
        return None


def stem_of(slot):
    return "p1_cover" if slot == "cover" else "p1_" + slot.replace("-", "_")


def browser_case(browser, origin, name, width, height, dpr, touch):
    context = browser.new_context(
        viewport={"width": width, "height": height},
        device_scale_factor=dpr,
        has_touch=touch,
        is_mobile=touch,
        reduced_motion="reduce",
    )
    context.route("**/*", lambda route: route.continue_() if route.request.url.startswith(origin + "/") else route.abort())
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    record = {"name": name, "viewport": [width, height], "dpr": dpr, "emulated_touch": touch, "figures": [], "screenshots": []}
    try:
        response = page.goto(origin + ROUTE, wait_until="domcontentloaded", timeout=30000)
        check(response is not None and response.status == 200, name + ": article HTTP status")
        page.wait_for_timeout(350)
        count = page.locator("figure.paper-figure--cinematic").count()
        check(count == 7, name + ": expected 7 semantic figures, got " + str(count))
        snap = page.evaluate("""() => ({
            scrollWidth: document.documentElement.scrollWidth,
            clientWidth: document.documentElement.clientWidth,
            contentWidth: document.querySelector('.paper-content')?.getBoundingClientRect().width || 0
        })""")
        record["document_width"] = snap
        check(snap["scrollWidth"] <= snap["clientWidth"] + 1, name + ": unwanted horizontal page scroll")
        record["screenshots"].append(safe_screenshot(page, name + "-article-top"))

        for slot in SLOTS:
            selector = 'figure[data-figure-slot="' + slot + '"]'
            fig = page.locator(selector)
            check(fig.count() == 1, name + ": missing or duplicated " + slot)
            if fig.count() != 1:
                continue
            img = fig.locator("img")
            fig.scroll_into_view_if_needed(timeout=15000)
            page.wait_for_function(
                "(sel) => { const i = document.querySelector(sel + ' img'); return !!i && i.complete && i.naturalWidth > 0; }",
                arg=selector,
                timeout=20000,
            )
            info = fig.evaluate("""(f) => {
                const img=f.querySelector('img'),a=f.querySelector('a.paper-figure-open'),
                      cap=f.querySelector('figcaption'),desc=f.querySelector('.figure-description'),
                      r=img.getBoundingClientRect(),cs=getComputedStyle(img);
                return {
                    slot:f.dataset.figureSlot, src:img.currentSrc, alt:img.alt,
                    naturalWidth:img.naturalWidth,naturalHeight:img.naturalHeight,
                    width:r.width,height:r.height,display:cs.display,
                    link:a?.href,label:a?.getAttribute('aria-label'),
                    target:a?.target,rel:a?.rel,describedBy:img.getAttribute('aria-describedby'),
                    descriptionId:desc?.id,description:desc?.textContent.trim(),
                    caption:cap?.textContent.trim(),loading:img.loading
                };
            }""")
            record["figures"].append(info)
            stem = stem_of(slot)
            check(stem + "_" in info["src"] and info["src"].endswith("q93.webp"), name + " " + slot + ": wrong compressed src/currentSrc")
            check(info["alt"] and len(info["alt"]) >= 25, name + " " + slot + ": missing meaningful alt")
            check(info["description"] and len(info["description"]) >= 60, name + " " + slot + ": missing long description")
            check(info["descriptionId"] == info["describedBy"], name + " " + slot + ": broken aria-describedby")
            check(info["caption"] and len(info["caption"]) >= 45, name + " " + slot + ": missing visible caption")
            check(info["link"].endswith(stem + "_master_1920x1080.png"), name + " " + slot + ": full-resolution link points to wrong image")
            check(info["target"] == "_blank" and "noopener" in (info["rel"] or ""), name + " " + slot + ": new-tab protection")
            check(info["label"] and "full-resolution" in info["label"].lower(), name + " " + slot + ": insufficient accessible link label")
            check(info["width"] > 100 and abs(info["width"] / info["height"] - 16 / 9) < 0.025, name + " " + slot + ": aspect ratio/cropping mismatch")
            check(info["src"].endswith(("_768w_q93.webp", "_1280w_q93.webp", "_1920w_q93.webp")), name + " " + slot + ": unlisted derivative")
            if slot == "cover":
                check(info["loading"] == "eager", name + ": cover should load eagerly")
            else:
                check(info["loading"] == "lazy", name + " " + slot + ": expected lazy loading")
            if slot == "figure-1-1":
                check("Λ = 0" in info["caption"] and "Λ = 0" in info["description"], name + ": Figure 1.1 Lambda caveat missing")
            if slot == "figure-2-1":
                check("fundamentally incompatible" not in info["caption"].lower(), name + ": outdated Figure 2.1 claim")
            if slot == "figure-5-1":
                check("untested hypothesis" in info["caption"].lower(), name + ": Figure 5.1 lacks untested caveat")
            if slot in ("figure-1-1", "figure-2-1", "figure-5-1") and dpr == 1:
                record["screenshots"].append(safe_screenshot(page, name + "-" + slot, selector))

        images = page.evaluate("""() => performance.getEntriesByType('resource')
            .filter(e => e.name.includes('/images/symmetria/paper-01/approved-20261120/') && e.name.endsWith('.webp'))
            .map(e => ({url:e.name,transferSize:e.transferSize,encodedBodySize:e.encodedBodySize,decodedBodySize:e.decodedBodySize}))""")
        selected = [f["src"] for f in record["figures"]]
        selected_set = set(selected)
        used = [e for e in images if e["url"] in selected_set]
        record["network"] = {
            "all_webp_entries": images,
            "selected_webp_entries": used,
            "selected_body_bytes": sum(e["encodedBodySize"] for e in used),
            "selected_transfer_bytes": sum(e["transferSize"] for e in used),
        }
        check(len(selected_set) == 7 and len(used) == 7, name + ": seven chosen WebPs not observed as network resources")
        check(all(e["encodedBodySize"] > 0 for e in used), name + ": invalid/missing browser measured body size")

        link = page.locator('figure[data-figure-slot="cover"] a.paper-figure-open')
        link.scroll_into_view_if_needed(timeout=10000)
        link.focus()
        focused = link.evaluate("(a) => document.activeElement === a")
        check(focused, name + ": cover full-resolution link not keyboard-focusable")
        if touch:
            with page.expect_popup(timeout=12000) as popup_info:
                link.tap(timeout=10000)
        else:
            with page.expect_popup(timeout=12000) as popup_info:
                page.keyboard.press("Enter")
        popup = popup_info.value
        popup.wait_for_load_state("domcontentloaded", timeout=20000)
        record["opened_full_resolution"] = popup.url
        check(popup.url.endswith("p1_cover_master_1920x1080.png"), name + ": zoom opens wrong content")
        popup.close()
        check(not errors, name + ": JS errors: " + repr(errors[:5]))
        record["page_errors"] = errors
    except Exception as exc:
        issues.append(name + ": browser exception: " + str(exc))
        record["exception"] = str(exc)
    finally:
        results.append(record)
        context.close()


def broken_image_case(browser, origin):
    context = browser.new_context(
        viewport={"width": 320, "height": 740},
        device_scale_factor=1,
        is_mobile=True,
        has_touch=True,
    )
    context.route("**/p1_figure_2_1_768w_q93.webp", lambda route: route.abort())
    context.route("**/*", lambda route: route.continue_() if route.request.url.startswith(origin + "/") else route.abort())
    page = context.new_page()
    record = {"name": "deliberate-image-failure-figure-2-1"}
    try:
        page.goto(origin + ROUTE, wait_until="domcontentloaded", timeout=30000)
        fig = page.locator('figure[data-figure-slot="figure-2-1"]')
        fig.scroll_into_view_if_needed(timeout=15000)
        page.wait_for_function(
            "() => {const i=document.querySelector('figure[data-figure-slot=\"figure-2-1\"] img');return !!i&&i.complete;}",
            timeout=15000,
        )
        record.update(fig.evaluate("""(f) => {
            const i=f.querySelector('img'),c=f.querySelector('figcaption'),d=f.querySelector('.figure-description');
            return {imageFailed:i.naturalWidth===0,currentSrc:i.currentSrc,
                    alt:i.alt,captionVisible:!!c&&c.getBoundingClientRect().width>0,
                    descriptionVisible:!!d&&d.getBoundingClientRect().width>0}
        }"""))
        check(record["imageFailed"], "broken-image test: abort did not fail chosen derivative")
        check(record["captionVisible"] and record["descriptionVisible"] and bool(record["alt"]), "broken-image test: text fallback absent")
        record["screenshot"] = safe_screenshot(page, "deliberate-broken-image-figure-2-1", 'figure[data-figure-slot="figure-2-1"]')
    except Exception as exc:
        issues.append("broken-image case: " + str(exc))
        record["exception"] = str(exc)
    finally:
        results.append(record)
        context.close()


def main():
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    origin = "http://127.0.0.1:" + str(server.server_port)
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True, args=["--no-sandbox"])
            try:
                for item in CASES:
                    browser_case(browser, origin, *item)
                broken_image_case(browser, origin)
            finally:
                browser.close()
    except Exception as exc:
        issues.append("fatal Chromium startup/browser failure: " + str(exc))
    finally:
        server.shutdown()
        server.server_close()
    output = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": sha,
        "article": ROUTE,
        "browser_type": "Playwright Chromium on isolated GitHub Actions runner",
        "no_external_deployment": True,
        "acceptance_status": "PASS" if not issues else "FAIL",
        "tests": results,
        "issues": issues,
        "notes": [
            "Responsive browser layouts, actual currentSrc, same-origin resource timing, keyboard activation, Chromium touch emulation and deliberate image failure.",
            "Mobile interaction is browser-emulated, not a physical handset; performance sizes are same-origin browser resource timing, not real-world cellular download latency.",
            "Artifact uploads are CI evidence only; no public preview or release is deployed.",
        ],
    }
    dest = OUTPUT / "p1-browser-acceptance.json"
    dest.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({
        "result": output["acceptance_status"],
        "commit": sha,
        "test_cases": len(results),
        "issues": len(issues),
        "issue_messages": issues,
        "artifact": str(dest.relative_to(ROOT)),
    }, indent=2, ensure_ascii=False))
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())
