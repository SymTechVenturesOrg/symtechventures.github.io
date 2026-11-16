from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import threading,functools,atexit,subprocess,re,json,hashlib,xml.etree.ElementTree as ET
from playwright.sync_api import sync_playwright
from urllib.request import urlopen
repo=Path(__file__).resolve().parents[3];server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(SimpleHTTPRequestHandler,directory=str(repo)));threading.Thread(target=server.serve_forever,daemon=True).start();atexit.register(server.shutdown);base=f'http://127.0.0.1:{server.server_port}'
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.img=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if d.get('id'):self.ids.add(d['id'])
  if t=='img':self.img.append(d)
  for k in ('href','src','action'):
   if d.get(k):self.refs.append((t,k,d[k]))
htmls=list(repo.rglob('*.html')); broken=[]; noalt=[]; external=[]; parsers={}
for f in htmls:
 p=Parser();p.feed(f.read_text(errors='ignore'));parsers[f]=p
 for im in p.img:
  if 'alt' not in im:noalt.append((str(f.relative_to(repo)),im.get('src')))
 for t,k,u in p.refs:
  parts=urlsplit(u)
  if parts.scheme == 'data':continue
  if parts.scheme in ('http','https','mailto','tel'):
   if parts.scheme in ('http','https'):external.append(u)
   continue
  if u.startswith('//'):continue
  target=(f.parent/parts.path.split('?')[0]).resolve() if parts.path else f
  if not target.exists():broken.append((str(f.relative_to(repo)),u))
  elif parts.fragment and target.suffix=='.html':
   dest=parsers.get(target)
   if dest is None:
    dest=Parser();dest.feed(target.read_text(errors='ignore'));parsers[target]=dest
   if parts.fragment not in dest.ids:broken.append((str(f.relative_to(repo)),u+' (fragment)'))
cssbroken=[]
for f in repo.rglob('*.css'):
 for u in re.findall(r'url\([\"\']?([^\)\"\']+)',f.read_text(errors='ignore')):
  if urlsplit(u).scheme or u.startswith('data:'):continue
  if not (f.parent/urlsplit(u).path).exists():cssbroken.append((str(f.relative_to(repo)),u))
assert not broken,broken[:30];assert not noalt,noalt[:20];assert not cssbroken,cssbroken
# Keep file blob checks relative to immutable main branch baseline.
hashes=[];after_hashes=[]
for i,expected in enumerate(['390a8676189542fc9044c1dabbbf344ad10e69f6','ec70f57a24f160e5971bad5fa4567529ef54bb79','90385bd2da97c75d0da3ebe17355753e762599ee','702e47f1883335c4a4202d71e10ad8da431a9d87'],1):
 f=repo/f'articles/symmetria/symmetria-paper-{i:02d}.html';actual=subprocess.check_output(['git','-C',str(repo),'hash-object',str(f)]).decode().strip();assert actual!=expected
 old=subprocess.check_output(['git','-C',str(repo),'show',f'origin/main:{f.relative_to(repo)}']).decode('utf8')
 normalized=f.read_text(encoding='utf8');normalized=re.sub(r'\n<a class="skip-to-content" href="#main-content">Skip to main content</a>','',normalized);normalized=re.sub(r'<main id="main-content">','<main>',normalized,count=1);assert normalized==old
 article=f.read_text(errors='ignore');imgs=re.findall(r'<img[^>]+src=[\"\']([^\"\']+)',article,re.I);assert len(imgs)==13
 for src in imgs: assert (f.parent/src).exists(),(f,src)
 hashes.append(expected);after_hashes.append(actual)
assert hashlib.sha256((repo/'CNAME').read_bytes()).hexdigest()=='01fe0273a99a8860d0f04ae48187b76388f0dfaf709972e19d6fa3c22c98275f'
smap=ET.parse(repo/'sitemap.xml').getroot();locs=[x.text for x in smap.findall('.//{*}loc')];assert len(locs)==16 and len(set(locs))==16
for loc in locs:
 path=urlsplit(loc).path;target=repo/'index.html' if path in ('','/') else repo/path.lstrip('/');assert target.exists(),loc
 with urlopen(base+path) as response:assert response.status==200,loc
for path in ['/pages/contact.html','/pages/enquiry.html','/pages/enquiry-thanks.html']+[f'/articles/symmetria/symmetria-paper-{i:02d}.html' for i in range(1,5)]:
 loc='https://www.symtechventures.com'+path;entry=next(x for x in smap.findall('{*}url') if x.find('{*}loc').text==loc);assert entry.find('{*}lastmod') is None,path
with urlopen(base+'/robots.txt') as response:assert response.status==200
with urlopen(base+'/sitemap.xml') as response:assert response.status==200

# Approved temporary suspension and archive indexing rules.
historic=['/pages/divisions.html','/pages/founding-fellows.html','/pages/symcore.html','/pages/symcraft.html','/pages/symcura.html','/pages/symlogic.html','/pages/symspace.html']
for path in historic:
 assert not any(urlsplit(loc).path==path for loc in locs),path
 html=(repo/path.lstrip('/')).read_text(encoding='utf8')
 assert '<meta name="robots" content="noindex,follow">' in html,path
 assert 'Historical page notice' in html,path
enquiry=(repo/'pages/enquiry.html').read_text(encoding='utf8')
contact=(repo/'pages/contact.html').read_text(encoding='utf8')
thanks=(repo/'pages/enquiry-thanks.html').read_text(encoding='utf8')
assert '<form' not in enquiry.lower()
assert 'method="POST"' not in enquiry and 'formsubmit.co' not in enquiry
assert '<input' not in enquiry.lower() and '<textarea' not in enquiry.lower()
assert 'not currently accepting enquiry submissions' in enquiry
assert 'View Enquiry Status' in contact
assert 'Opening this page does not mean a message has been sent.' in thanks
assert '<meta name="robots" content="noindex,follow">' in thanks
assert 'createAetherosShimmerHardReset' not in (repo/'js/main.js').read_text(encoding='utf8')
assert 'main p,.site-footer p{text-align:justify' in (repo/'css/v2-site.css').read_text(encoding='utf8')

# Actual Chromium checks over the full v2 shell and representative long paper at four widths.
principal=['/','/pages/research.html','/pages/symmetria.html','/pages/nsrp.html','/pages/seip.html','/pages/bridgepoint.html','/pages/discussion-series.html','/pages/publications.html','/pages/about.html','/articles/symmetria/symmetria-paper-01.html']
widths=[320,390,768,1440]; errors=[]; failed=[]; screenshots=[]; headings={}
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=browser.new_page(reduced_motion='reduce');page.set_default_timeout(15000)
 page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
 page.on('response',lambda r:failed.append((r.status,r.url)) if r.status>=400 and r.url.startswith(base) else None)
 for route in principal:
  response=page.goto(base+route,wait_until='networkidle');assert response.status==200,route
  title=page.title();assert title
  if route.startswith('/pages/') or route=='/':assert page.locator('h1').count()==1,(route,page.locator('h1').count())
  if route in ['/','/pages/research.html','/pages/symmetria.html','/pages/nsrp.html','/pages/seip.html','/pages/bridgepoint.html','/pages/discussion-series.html','/pages/publications.html','/pages/about.html']:
   expected=['Home','Research','BridgePoint','Discussion Papers','Publications','About']; got=[x.inner_text().strip() for x in page.locator('.main-nav a').all()];assert got==expected,(route,got)
   canonical=page.locator('link[rel=canonical]').get_attribute('href');assert canonical and canonical.startswith('https://www.symtechventures.com/'),(route,canonical);assert page.locator('meta[name=description]').get_attribute('content'),route
  headings[route]=page.locator('h1').count()
  assert page.locator('canvas').count()==0,('unexpected canvas/starfield',route)
  if route=='/':
   assert page.locator('main p').first.evaluate('(x)=>getComputedStyle(x).textAlign')=='justify'
   assert page.locator('.hero').evaluate('(x)=>getComputedStyle(x,"::before").backgroundImage')=='none'
  if route in ['/','/pages/research.html','/pages/symmetria.html','/pages/nsrp.html','/pages/seip.html','/pages/bridgepoint.html','/pages/discussion-series.html','/pages/publications.html','/pages/about.html','/articles/symmetria/symmetria-paper-01.html']:
   levels=page.locator('h1,h2,h3,h4,h5,h6').evaluate_all('(els)=>els.map(e=>Number(e.tagName[1]))');assert levels and levels[0]==1 and max([b-a for a,b in zip(levels,levels[1:])] or [0])<=1,(route,levels)
  for w in widths:
   page.set_viewport_size({'width':w,'height':900 if w>500 else 844}); page.wait_for_timeout(50)
   dims=page.evaluate('({client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth})');assert dims['client']==dims['scroll'],(route,w,dims)
   if w==390 and route in ['/','/pages/about.html','/pages/publications.html','/pages/discussion-series.html','/articles/symmetria/symmetria-paper-01.html']:
    filename='postapproval-'+('home' if route=='/' else route.strip('/').replace('/','-').replace('.html',''))+'-390.png';dest=repo/'docs/reports/screenshots'/filename;page.screenshot(path=str(dest),full_page=True,timeout=30000);screenshots.append(str(dest.relative_to(repo)))
   if w==1440 and route in ['/','/pages/about.html','/pages/publications.html','/pages/discussion-series.html','/articles/symmetria/symmetria-paper-01.html']:
    filename='postapproval-'+('home' if route=='/' else route.strip('/').replace('/','-').replace('.html',''))+'-1440.png';dest=repo/'docs/reports/screenshots'/filename;page.screenshot(path=str(dest),full_page=True,timeout=30000);screenshots.append(str(dest.relative_to(repo)))
  # Keyboard disclosure test at phone width: skip link -> brand -> summary, open, Escape closes and restores focus.
  if route=='/pages/about.html':
   page.set_viewport_size({'width':390,'height':844});page.goto(base+route,wait_until='networkidle');page.keyboard.press('Tab');assert page.evaluate('document.activeElement.className')=='skip';assert page.evaluate('getComputedStyle(document.activeElement).outlineStyle')=='solid'
   page.keyboard.press('Tab');page.keyboard.press('Tab');assert page.evaluate('document.activeElement.tagName')=='SUMMARY'
   page.keyboard.press('Enter');assert page.locator('.mobile-nav').evaluate('(x)=>x.open');
   menu_labels=[]
   for _ in range(6):
    page.keyboard.press('Tab');menu_labels.append(page.evaluate('document.activeElement.innerText.trim()'))
   assert menu_labels==['Home','Research','BridgePoint','Discussion Papers','Publications','About'],menu_labels
   page.keyboard.press('Escape');assert not page.locator('.mobile-nav').evaluate('(x)=>x.open');assert page.evaluate('document.activeElement.tagName')=='SUMMARY'
   motion=page.evaluate("({behavior:getComputedStyle(document.documentElement).scrollBehavior,animation:getComputedStyle(document.body,'::before').animationName,bg:getComputedStyle(document.body,'::before').backgroundImage})");assert motion['behavior']=='auto' and motion['animation']=='none' and motion['bg']=='none',motion
   touch=page.locator('.mobile-nav summary').bounding_box();assert touch['height']>=24 and touch['width']>=24,touch
  if route=='/pages/discussion-series.html':assert page.locator('.category').count()==4 and page.locator('.lesson-card').count()==16 and page.locator('.lesson-card a').count()==4 and page.locator('.lesson-card:not(:has(a))').count()==12
  if route=='/pages/bridgepoint.html':assert page.locator('.category').count()==4 and page.locator('.lesson-card').count()==16 and page.locator('.lesson-card a').count()==0 and all('planned' in x.lower() for x in page.locator('.lesson-card').all_inner_texts())
  if route=='/pages/nsrp.html':assert page.locator('.project').count()==5 and page.locator('.phase').count()==20 and 'provisional' in page.locator('.status-note').inner_text().lower()
  if route=='/pages/seip.html':assert page.locator('.project').count()==5 and page.locator('.phase').count()==20
  if route=='/pages/publications.html':assert page.locator('.publication-record').count()==0 and page.locator('article').count()==0 and page.get_by_text('No formal research publications listed yet. This section will be updated when work is ready for public release.').count()==1
  if route in ['/pages/divisions.html','/pages/founding-fellows.html','/pages/symcore.html','/pages/symcraft.html','/pages/symcura.html','/pages/symlogic.html','/pages/symspace.html']:
   assert page.locator('[aria-label="Historical page notice"]').count()==1,route
   assert page.locator('meta[name="robots"]').get_attribute('content')=='noindex,follow',route
   if route=='/pages/founding-fellows.html':
    page.set_viewport_size({'width':1440,'height':900});pathshot=repo/'docs/reports/screenshots/postapproval-legacy-fellows-1440.png';page.screenshot(path=str(pathshot),full_page=True,timeout=30000);screenshots.append(str(pathshot.relative_to(repo)))
    page.set_viewport_size({'width':390,'height':844});pathshot=repo/'docs/reports/screenshots/postapproval-legacy-fellows-390.png';page.screenshot(path=str(pathshot),full_page=True,timeout=30000);screenshots.append(str(pathshot.relative_to(repo)))
 legacy_paths=['/pages/divisions.html','/pages/founding-fellows.html','/pages/symcore.html','/pages/symcraft.html','/pages/symcura.html','/pages/symlogic.html','/pages/symspace.html','/pages/contact.html','/pages/enquiry.html','/pages/enquiry-thanks.html']+[f'/articles/symmetria/symmetria-paper-{i:02d}.html' for i in range(1,5)]
 for route in legacy_paths:
  response=page.goto(base+route,wait_until='networkidle');assert response.status==200,route
  assert page.locator('.skip-to-content').count()==1,route
  assert page.locator('canvas').count()==0,('unexpected canvas',route)
  if route=='/pages/enquiry.html':
   assert page.locator('form,input,textarea,button[type=submit]').count()==0
   assert page.get_by_text('Online enquiries are temporarily unavailable').count()==1
  if route=='/pages/enquiry-thanks.html':
   assert page.get_by_text('Opening this page does not mean a message has been sent.',exact=False).count()==1
  page.keyboard.press('Tab');assert page.evaluate('document.activeElement.className')=='skip-to-content',route
  assert page.evaluate('getComputedStyle(document.activeElement).outlineStyle')=='solid',route
  if route in ['/pages/divisions.html','/pages/founding-fellows.html','/pages/symcore.html','/pages/symcraft.html','/pages/symcura.html','/pages/symlogic.html','/pages/symspace.html']:
   assert page.locator('[aria-label="Historical page notice"]').count()==1,route
   if route=='/pages/founding-fellows.html':
    page.set_viewport_size({'width':1440,'height':900});pathshot=repo/'docs/reports/screenshots/postapproval-legacy-fellows-1440.png';page.screenshot(path=str(pathshot),full_page=True,timeout=30000);screenshots.append(str(pathshot.relative_to(repo)))
    page.set_viewport_size({'width':390,'height':844});pathshot=repo/'docs/reports/screenshots/postapproval-legacy-fellows-390.png';page.screenshot(path=str(pathshot),full_page=True,timeout=30000);screenshots.append(str(pathshot.relative_to(repo)))
  for w in [320,390,768,1440]:
   page.set_viewport_size({'width':w,'height':900 if w>500 else 844});dims=page.evaluate('({client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth})')
   assert dims['client']==dims['scroll'],(route,w,dims)
 browser.close()
assert not errors,errors;assert not failed,failed
print(json.dumps({'html_files':len(htmls),'local_ref_failures':broken,'missing_alt':noalt,'css_ref_failures':cssbroken,'screenshots':screenshots,'browser_routes':principal+legacy_paths,'viewports':widths,'catalogues':'discussion 4/4 linked/12 planned; bridgepoint 4/16/zero links; NSRP 5/20 provisional; SEIP 5/20; publications zero','errors':errors,'failed_local_responses':failed,'paper_hashes_before':hashes,'paper_hashes_after':after_hashes,'sitemap':len(locs)}))
