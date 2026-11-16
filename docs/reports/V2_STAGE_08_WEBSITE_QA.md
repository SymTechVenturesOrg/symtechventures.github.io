# SymTech Ventures v2.0 — Stage 8 Website QA

**Date:** 16 November 2026 (GMT)
**Branch:** `feature/v2-space-research-website`
**Starting head:** `13f668358d3946efad13a47b338955b9443813fc`
**Scope:** Website quality, accessibility, compatibility and legacy review only. No lessons were developed or changed.

## Decision

**Not ready for owner release review.** The Stage 8 implementation fixes below are in the draft PR, but contact-form privacy/anti-spam decisions, indexing policy for legacy pages, and image/figure rights review remain open release concerns. No merge or deployment occurred.

## P1 release blockers and owner decisions

1. **Contact form privacy and processing:** the existing enquiry form posts to a third-party processor, has no visible privacy/data-handling notice, and has its anti-spam CAPTCHA setting disabled. I did not submit the form or send personal data. Delivery, processor retention, consent wording and spam handling remain unverified. Owner review must decide whether the form stays and provide approved disclosure/handling before release. Recipient details are omitted from this report.
2. **Legacy search indexing:** visible historical-context notices now clarify the old Founding Fellows/division pages, while preserving all URLs. These pages remain in the 23-entry sitemap and `robots.txt` allows crawling. Owner must decide whether to keep them indexed, remove them from the sitemap, or apply a reviewed `noindex` approach. No redirect or indexing policy was silently applied.
3. **Asset rights and paper figures:** provenance/redistribution rights for existing logos and illustrations are unverified. Mathematical text embedded in paper illustrations has not been independently checked. Owner clearance is still needed.
4. **External profile reachability:** a read-only HEAD request to the supplied LinkedIn URL returned HTTP **999** from this environment. The link is present and syntactically correct; external reachability could not be confirmed here.

## Fixes applied

- Added a keyboard-operable Escape dismissal to the shared mobile disclosure menu; closing it returns focus to its summary control.
- Added visible skip-to-main-content links to preserved legacy pages, Contact/enquiry/thank-you, and the four article shells. Each targets the main content landmark; original article bodies remain byte-for-byte identical after removing only these wrapper additions.
- Added a clearly labelled historical-project notice to Divisions, Founding Fellows and all five old division pages. The pages and incoming URLs remain available.
- Added a small root favicon after Chromium reported `/favicon.ico` missing on original article shells.
- Removed stale `lastmod` dates from sitemap entries for the 14 pages whose wrapper/legacy context changed; no replacement dates were invented.

## Verification matrix

| Area | Result | Evidence |
| --- | --- | --- |
| Full local reference scan | **PASS** | All 36 HTML files checked; no missing relative HTML links, fragments, `src`/`action` files, CSS `url()` resources, or missing image `alt` attributes. |
| Browser routes/resources | **PASS** | 23 unique routes across v2 pages, legacy pages and four papers loaded in Chromium; zero failed local responses, page errors or console errors. All 23 sitemap destinations returned HTTP 200 locally. |
| Device layout | **PASS** | Primary pages, representative long Paper 1, and legacy routes checked at 320, 390, 768 and 1440px; no horizontal overflow. |
| Navigation and keyboard | **PASS, targeted** | Six v2 nav labels; skip link gets first focus and visible outline; mobile menu opens, tabs through all six links, Escape closes it and restores focus. Legacy/article skip links are first focus and target `main`. |
| Reduced motion and starfield | **PASS, targeted** | Reduced-motion Chromium reports `scroll-behavior:auto`; starfield is static CSS with no canvas, animation loop or runtime particle work. Stars are visible in Home/About screenshots. CPU/memory profiling was not run because the implementation is static. |
| Contrast and touch targets | **PASS, spot checks only** | Computed sample contrast: page lead 12.1:1, status note 11.9:1, status highlight 13.24:1, link 13.57:1. Mobile menu summary measured 79×42px. This is not a full contrast or WCAG audit. |
| Programme/status accuracy | **PASS** | BridgePoint 4 categories/16 Planned entries/zero lesson links; NSRP 5 projects/20 phases with NCP provisional notice; SEIP 5/20; Discussion Papers 4 categories, 4 linked online essays and 12 Planned unlinked entries; Publications has zero records. |
| Article integrity | **PASS, wrapper-only change** | Four original article paths and all 13 image references per paper remain. Main-branch bodies compare byte-for-byte after removing only the new skip-link and `main` id wrapper additions. Exact before/after blob hashes follow below. |
| Sitemap/metadata | **PASS with owner decision pending** | Sitemap parses as XML, has 23 unique existing local paths, and each returns HTTP 200. V2 routes have titles, descriptions and canonical URLs. `CNAME` SHA-256 remains `01fe0273a99a8860d0f04ae48187b76388f0dfaf709972e19d6fa3c22c98275f`. `robots.txt` allows crawling and references the sitemap. V2 pages do not currently define Open Graph tags. Legacy indexing policy remains open. |
| Form privacy/external services | **BLOCKED / NOT SUBMITTED** | Form markup reviewed only; no personal information submitted and no third-party delivery test. LinkedIn HEAD returned 999 from this environment. |
| Assistive technology / automated WCAG | **NOT RUN** | No screen-reader session or axe-core package was available. Do not treat these checks as accessibility certification. |

## Article hashes and preservation

| Article | Before (main) | After wrapper-only accessibility update |
| --- | --- | --- |
| Paper 1 | `390a8676189542fc9044c1dabbbf344ad10e69f6` | `a9d89172a6549b5a26451f2745f1d032659dd32e` |
| Paper 2 | `ec70f57a24f160e5971bad5fa4567529ef54bb79` | `5c94104eef059a18f202768df99591e3050ba50d` |
| Paper 3 | `90385bd2da97c75d0da3ebe17355753e762599ee` | `07395d1d309dbe113ca2ed43ebf4bb633af2162f` |
| Paper 4 | `702e47f1883335c4a4202d71e10ad8da431a9d87` | `0d259414c78c9e1bc8ddaf60f8832a81607b2141` |

Exact diff per article is one skip link before the header and `id="main-content"` on its `<main>` element. Removing those two wrapper changes yields exact original bytes. Paper text, figures, image sources and public URLs were not changed.

## Legacy-file before/after blob hashes

The only content added to these pages is a short historical-context notice immediately after `<main>`; their prior body remains in place.

| Page | Before (main) | After |
| --- | --- | --- |
| `pages/divisions.html` | `d8d9dfa07471647b95dfe856ed9a9af41b37f63e` | `dd38e7458ae0b1ac836a02dccfa20c9f9ba7491d` |
| `pages/founding-fellows.html` | `764a1822cb7a2705694a2d6a0a6d8567352494ea` | `9193b811d6502f93a8c39b5d5b06bcf975db9458` |
| `pages/symcore.html` | `92612dff4389007c3b08b9c60d4d5ec694443714` | `bbf88dd1001f82adf551b31342d69ab4541c4fed` |
| `pages/symcraft.html` | `8396689a82c48e5c8ff06ee00729dfe9dc632813` | `a544de8f5f68de6b02245fc14e225afc4956fe4a` |
| `pages/symcura.html` | `fe18d76bba9d96a6510747fb7e8e3d9abd872c57` | `eaa274e95d41c923c0d07456140399017873c498` |
| `pages/symlogic.html` | `37b7f7ca4668f044079af19e98041b7a393c023e` | `9fc23ec623e188f75ce84b7164e6e8aedb4e7596` |
| `pages/symspace.html` | `8fbadba3e0847105d10e50485adaf671de1d84d8` | `9cef67e2faba0ee94f4a804634a0190f7b1377e8` |

Contact, enquiry and thank-you page hash changes are only the new skip link and main-content target. Form action, fields and processor configuration were left unchanged. No private recipient value is reproduced here.

## Screenshots from this QA run

- Home: `docs/reports/screenshots/stage8-home-1440.png`, `stage8-home-390.png`
- Discussion Papers: `stage8-pages-discussion-series-1440.png`, `stage8-pages-discussion-series-390.png`
- Publications: `stage8-pages-publications-1440.png`, `stage8-pages-publications-390.png`
- About: `stage8-pages-about-1440.png`, `stage8-pages-about-390.png`
- Representative long paper: `stage8-articles-symmetria-symmetria-paper-01-1440.png`, `stage8-articles-symmetria-symmetria-paper-01-390.png`
- Historical context notice: `stage8-legacy-fellows-1440.png`, `stage8-legacy-fellows-390.png`

Screenshots are actual local Chromium captures, with mobile menus closed by default.

## Reproduction

With Python 3.12, Playwright and system Chromium available, run:

```sh
python3 docs/reports/scripts/v2_stage8_qa.py
```

The script starts a temporary localhost server, checks all HTML/CSS local references and image alt attributes, sitemap destinations and article hashes, then tests the v2 shell and representative long article plus legacy routes at four viewport widths.

## Remaining review priorities

- **P1:** Resolve form privacy, third-party processing and anti-spam settings; decide legacy indexing treatment; clear asset rights and embedded mathematical figures.
- **P2:** Owner review of the static-starfield appearance and historical-page notice screenshots; confirm legacy indexing policy.
- **P3:** Add Open Graph metadata if desired; run automated accessibility tooling and assistive-technology/manual WCAG review; profile real-device performance if animation is ever introduced.
