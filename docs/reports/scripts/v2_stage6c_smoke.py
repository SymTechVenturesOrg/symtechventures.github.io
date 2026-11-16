from playwright.sync_api import sync_playwright
from urllib.request import urlopen
from pathlib import Path
import json,xml.etree.ElementTree as ET,subprocess,re,hashlib,threading,atexit,functools
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
repo=Path(__file__).resolve().parents[3]; server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(SimpleHTTPRequestHandler,directory=str(repo))); threading.Thread(target=server.serve_forever,daemon=True).start(); atexit.register(server.shutdown); base=f'http://127.0.0.1:{server.server_port}'; errors=[]
nav=['Home','Research','BridgePoint','Discussion Papers','Publications','About']
routes=['/','/pages/research.html','/pages/bridgepoint.html','/pages/discussion-series.html','/pages/publications.html','/pages/about.html']
expected_titles=['SymTech Ventures | Independent Space-Focused Research','Research | SymTech Ventures','BridgePoint | Learn the Mathematics of Physics','SYMMETRIA Discussion Papers | SymTech Ventures','Publications | SymTech Ventures','About | SymTech Ventures']
legacy=['/pages/divisions.html','/pages/founding-fellows.html','/pages/symcore.html','/pages/symcraft.html','/pages/symcura.html','/pages/symlogic.html','/pages/symspace.html','/pages/contact.html','/pages/enquiry.html','/pages/enquiry-thanks.html']
for path in routes+legacy+['/pages/symmetria.html','/pages/nsrp.html','/pages/seip.html']+[f'/articles/symmetria/symmetria-paper-{i:02d}.html' for i in range(1,5)]:
 with urlopen(base+path) as r: assert r.status==200 and r.read(),path
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox']); page=b.new_page(reduced_motion='reduce');page.set_default_timeout(5000)
 page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
 for path in routes:
  resp=page.goto(base+path,wait_until='networkidle');assert resp.status==200
  assert page.locator('.main-nav a').count()==6,path
  assert page.title()==expected_titles[routes.index(path)],(path,page.title())
  labels=[x.inner_text().strip() for x in page.locator('.main-nav a').all()];assert labels==nav,(path,labels)
  page.keyboard.press('Tab');assert page.evaluate('document.activeElement.className')=='skip',path
  assert page.evaluate('getComputedStyle(document.activeElement).outlineStyle')=='solid',path
  page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth===document.documentElement.clientWidth'),path
  page.locator('.mobile-nav summary').click();assert page.locator('.mobile-nav').evaluate('(x)=>x.open');page.locator('.mobile-nav summary').click()
  page.set_viewport_size({'width':320,'height':844});assert page.evaluate('document.documentElement.scrollWidth===document.documentElement.clientWidth'),path
  if path in ['/pages/about.html','/pages/publications.html','/pages/discussion-series.html']:
   page.set_viewport_size({'width':1440,'height':900});page.screenshot(path=str(repo/'docs/reports/screenshots'/('stage6c-'+Path(path).stem+'-desktop.png')),full_page=True)
   page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(repo/'docs/reports/screenshots'/('stage6c-'+Path(path).stem+'-390px.png')),full_page=True)
  # Static starfield and reduced-motion behavior.
  if path=='/pages/about.html':
   vals=page.evaluate("({bg:getComputedStyle(document.body,'::before').backgroundImage,scroll:getComputedStyle(document.documentElement).scrollBehavior,transition:getComputedStyle(document.querySelector('.content-card')||document.body).transitionDuration})")
   assert vals['bg']!='none' and vals['scroll']=='auto',vals
 page.goto(base+'/pages/discussion-series.html',wait_until='networkidle')
 assert page.locator('.category').count()==4
 assert page.locator('.lesson-card').count()==16
 assert page.locator('.lesson-card a').count()==4
 assert page.locator('.lesson-card:not(:has(a))').count()==12
 for path,n in [('/pages/bridgepoint.html',16),('/pages/nsrp.html',20),('/pages/seip.html',20)]:
  page.goto(base+path,wait_until='networkidle');sel='.lesson-card' if 'bridgepoint' in path else '.phase';assert page.locator(sel).count()==n
 page.goto(base+'/pages/publications.html');assert page.get_by_text('No formal research publications listed yet. This section will be updated when work is ready for public release.').count()==1
 assert not errors,errors
 b.close()
# sitemap XML and URL domain/page presence
smap=ET.parse(repo/'sitemap.xml').getroot(); locs=[x.text for x in smap.findall('{*}url/{*}loc')]
assert len(locs)==len(set(locs))
for path in routes[1:]+[f'/articles/symmetria/symmetria-paper-{i:02d}.html' for i in range(1,5)]: assert 'https://www.symtechventures.com'+path in locs,path
# Modified/new v2 pages have no unverifiable lastmod date.
for path in ['/','/pages/research.html','/pages/symmetria.html','/pages/nsrp.html','/pages/seip.html','/pages/bridgepoint.html','/pages/discussion-series.html','/pages/publications.html','/pages/about.html']:
 loc='https://www.symtechventures.com'+path
 element=next(el for el in smap.findall('{*}url') if el.find('{*}loc').text==loc)
 assert element.find('{*}lastmod') is None,path
for i,expected in enumerate(['390a8676189542fc9044c1dabbbf344ad10e69f6','ec70f57a24f160e5971bad5fa4567529ef54bb79','90385bd2da97c75d0da3ebe17355753e762599ee','702e47f1883335c4a4202d71e10ad8da431a9d87'],1):
 path=f'articles/symmetria/symmetria-paper-{i:02d}.html'
 actual=subprocess.check_output(['git','-C',str(repo),'hash-object',str(repo/path)]).decode().strip();assert actual==expected,(path,actual)
 article=(repo/path).read_text(errors='ignore'); images=re.findall(r'<img[^>]+src=[\"\']([^\"\']+)',article,re.I)
 assert len(images)==13,(path,len(images))
 for src in images: assert ((repo/path).parent/src).exists(),(path,src)
assert hashlib.sha256((repo/'CNAME').read_bytes()).hexdigest()=='01fe0273a99a8860d0f04ae48187b76388f0dfaf709972e19d6fa3c22c98275f'

print(json.dumps({'nav_routes_200':routes,'legacy_routes_200':legacy,'catalogues':'discussion 4 categories/4 online/12 planned; bridgepoint 4/16; nsrp 5/20; seip 5/20','viewport_checks':'all six nav destinations at 390 and 320; screenshots 1440 and 390 for About/Publications/Discussion','sitemap_entries':len(locs),'article_hashes':'unchanged','console_errors':errors}))
