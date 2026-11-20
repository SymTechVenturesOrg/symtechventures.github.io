from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
import threading, json, math

root=Path(__file__).resolve().parents[3]
server=ThreadingHTTPServer(('127.0.0.1',0), partial(SimpleHTTPRequestHandler,directory=str(root)))
threading.Thread(target=server.serve_forever,daemon=True).start()
origin=f'http://127.0.0.1:{server.server_port}'
cases=[('desktop',1440,900,False),('portrait',390,844,True),('landscape',844,390,True)]
results=[]
with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    for mode,width,height,mobile in cases:
        context=browser.new_context(viewport={'width':width,'height':height},device_scale_factor=1,is_mobile=mobile,has_touch=mobile,reduced_motion='reduce')
        for number in range(1,5):
            route=f'/articles/symmetria/symmetria-paper-{number:02d}.html'
            page=context.new_page()
            r=page.goto(origin+route,wait_until='networkidle')
            assert r.status==200,(route,mode,r.status)
            figures=page.locator('.paper-content img')
            links=page.locator('.paper-content a.paper-figure-open')
            assert figures.count()==7 and links.count()==7,(route,mode,'figure count',figures.count(),links.count())
            dataset=page.evaluate("""() => [...document.querySelectorAll('.paper-content a.paper-figure-open')].map(a=>({
                href:a.href,target:a.target,rel:a.rel,label:a.getAttribute('aria-label'),imageSrc:a.querySelector('img')?.src,
                imageAlt:a.querySelector('img')?.alt,hint:a.querySelector('.paper-figure-open-label')?.textContent.trim()
            }))""")
            for row in dataset:
                assert '/pages/figure-viewer.html?' in row['href'] and 'src=images%2Fsymmetria%2Fpaper-0' in row['href'],(route,mode,'viewer link',row)
                assert row['target']=='_blank' and 'noopener' in row['rel'] and row['label'].startswith('Open interactive image viewer in a new tab: '),(route,mode,'semantics',row)
                assert row['hint']=='Open interactive image viewer ↗' and row['imageSrc'].endswith('.webp'),(route,mode,'source',row)
            assert page.evaluate('document.documentElement.scrollWidth<=document.documentElement.clientWidth'),(route,mode,'article overflow')
            first=links.first
            first.scroll_into_view_if_needed()
            if number==2 and mode in ['portrait','landscape']:
                page.screenshot(path=str(root/'phase2-qa-artifacts'/f'paper02-interactive-viewer-link-{mode}-{width}x{height}.png'),full_page=False)
            current_url=page.url
            if mobile:
                with page.expect_popup() as popup: first.tap()
            else:
                first.focus()
                assert first.evaluate('(a)=>a===document.activeElement')
                with page.expect_popup() as popup: page.keyboard.press('Enter')
            opened=popup.value
            opened.wait_for_load_state('networkidle')
            assert '/pages/figure-viewer.html?' in opened.url,(route,mode,'viewer URL',opened.url)
            assert page.url==current_url,(route,mode,'original tab changed')
            stage=opened.locator('#image-stage')
            viewerImage=opened.locator('#full-image')
            assert stage.is_visible(),(route,mode,'stage missing')
            assert opened.locator('#original-image').get_attribute('href')==dataset[0]['imageSrc'],(route,mode,'original source')
            assert viewerImage.evaluate('(im)=>im.complete && im.naturalWidth>0 && im.naturalHeight>0'),(route,mode,'image load')
            assert viewerImage.get_attribute('alt')==dataset[0]['imageAlt'],(route,mode,'alt mismatch')
            initial=viewerImage.bounding_box()['width']
            assert initial>0,(route,mode,'initial image hidden')
            opened.locator('#zoom-in').click()
            assert viewerImage.bounding_box()['width']>initial*1.15,(route,mode,'button zoom failed')
            opened.locator('#zoom-fit').click()
            assert math.isclose(viewerImage.bounding_box()['width'],initial,rel_tol=.01),(route,mode,'fit failed')
            opened.locator('#zoom-actual').click()
            assert abs(viewerImage.bounding_box()['width']-viewerImage.evaluate('(im)=>im.naturalWidth'))<2,(route,mode,'100% original pixel zoom failed')
            opened.locator('#zoom-fit').click()
            if not mobile:
                rect=stage.bounding_box()
                opened.mouse.move(rect['x']+rect['width']/2,rect['y']+rect['height']/2)
                opened.mouse.wheel(0,-500)
                assert viewerImage.bounding_box()['width']>initial*1.5,(route,mode,'mouse wheel zoom failed')
                opened.mouse.wheel(0,500)
                assert viewerImage.bounding_box()['width']<initial*1.25,(route,mode,'wheel zoom-out failed')
                opened.locator('#zoom-actual').click()
                opened.locator('#zoom-in').click()
                before=viewerImage.bounding_box()['x']
                rect=stage.bounding_box()
                opened.mouse.move(rect['x']+rect['width']/2,rect['y']+rect['height']/2)
                opened.mouse.down()
                opened.mouse.move(rect['x']+rect['width']/2+105,rect['y']+rect['height']/2,steps=5)
                opened.mouse.up()
                if viewerImage.bounding_box()['width']>rect['width']+5:
                    assert abs(viewerImage.bounding_box()['x']-before)>5,(route,mode,'drag-to-pan failed')
            else:
                opened.locator('#zoom-fit').click()
                before=viewerImage.bounding_box()['width']
                opened.evaluate("""() => {
                  const s=document.querySelector('#image-stage'),r=s.getBoundingClientRect(),x=r.left+r.width/2,y=r.top+r.height/2;
                  const send=(type,id,px,py)=>s.dispatchEvent(new PointerEvent(type,{pointerId:id,pointerType:'touch',clientX:px,clientY:py,bubbles:true}));
                  send('pointerdown',11,x-40,y);send('pointerdown',12,x+40,y);
                  send('pointermove',12,x+100,y);send('pointerup',11,x-40,y);send('pointerup',12,x+100,y);
                }""")
                assert viewerImage.bounding_box()['width']>before*1.4,(route,mode,'pinch zoom simulation failed')
            opened.locator('#zoom-fit').click()
            assert not opened.evaluate('document.documentElement.scrollWidth>document.documentElement.clientWidth'),(route,mode,'viewer overflow')
            if number==2 and mode in ['desktop','portrait','landscape']:
                opened.screenshot(path=str(root/'phase2-qa-artifacts'/f'paper02-image-viewer-{mode}-{width}x{height}.png'),full_page=False)
            opened.close()
            results.append({'paper':number,'mode':mode,'width':width,'height':height,'links':len(dataset),'viewer':'decoded original WebP','zoom':'PASS'})
            page.close()
        context.close()
    # Disallow external image origins and path traversal via user-controlled viewer query.
    page=browser.new_page()
    response=page.goto(origin+'/pages/figure-viewer.html?src=https%3A%2F%2Fevil.example%2Ftracking.webp',wait_until='load')
    assert response.status==200
    assert page.locator('#viewer-error').is_visible() and page.locator('#original-image').is_hidden()
    assert page.locator('#full-image').get_attribute('src')==''
    page.close()
    browser.close()
server.shutdown()
assert len(results)==12 and sum(x['links'] for x in results)==84
print(json.dumps({'status':'PASS','route_modes':len(results),'links_verified':84,'mouse_wheel_zoom':True,
  'zoom_buttons':True,'drag_pan':True,'simulated_touch_pinch':True,'invalid_external_src_rejected':True,'results':results},indent=2))
