# SymTech Ventures v2.0 — Stage 8C: Raster Homepage Hero and Visual Regression

**Scope:** Finish the owner's approved **professional, restrained website presentation**, with a raster homepage hero and v2-style Contact and four preserved SYMMETRIA articles. This is a bounded implementation/QA checkpoint, **not a deployment instruction**.

**Repo:** `SymTechVenturesOrg/symtechventures.github.io`  
**Implementation branch:** `feature/v2-space-research-website`  
**Existing open draft PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5) — reuse it; no duplicate PR.  
**Latest Chat commit when brief prepared:** `e9ff8f5280d0edfa3d52f70400f95efc709a6190`; inspect current HEAD before editing.

## Owner's approved direction

- **Modern, credible, clean and grounded** independent space-exploration research website, retaining dark navy, elegant typography and restrained cyan/gold detail.
- A **raster Earth-at-sunrise image** rather than the existing inline SVG orbit drawing on the homepage. Preserve the current, editorially reviewed homepage wording and its six navigation links.
- Source workflow: **PNG master → self-hosted WebP, quality 80**; no text, buttons or fake scientific data baked into the image.
- Main paragraphs remain **fully justified** with hyphenation; headings, menus and controls naturally aligned.
- **No starfield** and no flashy photo montage or fictional operational machinery.
- Individual BridgePoint lessons remain **unwritten/Planned**; no new physics claims.

## Work already completed in Chat — VERIFY, DO NOT REDO FROM SCRATCH

1. `pages/contact.html` was rebuilt on this branch with `v2-site.css`, `v2-programmes.css`, six-link navigation, the v2 footer and a clear **enquiries paused** notice; the old third-party form is still removed. No source from the v1 layout remains on Contact.
2. All **four** `articles/symmetria/symmetria-paper-0[1-4].html` now use the v2 header/nav/footer and new stylesheet `css/v2-articles.css` after their legacy article stylesheet. Chat compared each complete `<main id="main-content">...</main>` block to the earlier Stage 8B commit `4dc5c4252ae0a3fc59ec9caf3bc64c67ba7e003c`: **every main block was byte-for-byte identical, including seven per-paper illustrations and the original article content**.
3. `docs/reports/scripts/v2_stage8_qa.py` was updated to compare **paper main bodies and seven figure references** rather than expecting unchanged full HTML blobs or old 13-image icon navigation; it also checks the new Contact page and all four articles.
4. A WebP converter `tools/prepare_homepage_webp.py` was added with Pillow quality 80. The **approved PNG and WebP binary exist in the originating Chat conversation**, but **they are NOT YET PRESENT in this GitHub branch**. Do not claim that binary upload happened.

## A. Complete the homepage raster artwork

**First obtain the exact owner-reviewed Earth-at-sunrise source file** as an attachment to this execution or from a source the operator explicitly provides. The Chat source asset is a **716×494 PNG**, the Chat-prepared **WebP quality 80 is 48,340 bytes** with SHA-256:

`b80e474a511d927e3ca3bea5f4bd3ab8795c394014353592ae5a15d13f4330f0`

It is **AI-generated conceptual Earth imagery**, not a NASA mission photograph; do not credit NASA, imply an authentic observation or make claims about its origin.

1. Confirm received binary and digest if using the prepared WebP. If the approved PNG is supplied instead, run `python3 tools/prepare_homepage_webp.py <approved-file.png> --output images/heroes/earthrise_hero_q80.webp`. Validate the WebP is actually a WebP, 716×494, and close to the expected size.
2. Commit the real binary at `images/heroes/earthrise_hero_q80.webp` to **the same feature branch**. A PNG master may be retained separately with clear naming, but avoid unnecessary source bloat in web-serving folders.
3. In `index.html`, replace **only the homepage `.orbit-wrap` inline SVG graphic** with the self-hosted WebP `<img>` element (actual responsive width/height, `loading="eager"`, `decoding="async"`, `fetchpriority="high"`). Use factual alt text such as **"Conceptual image of Earth's curved horizon at sunrise, viewed from orbit"**; a small credit may read **"Conceptual illustration"**. Preserve the "Questions before conclusions" overlay/caption if it reads well.
4. Adjust `css/v2-site.css` from `.orbit-wrap svg` to `.orbit-wrap img`, maintain the approved dark theme, rounded/subtle frame and appropriate mobile crop. Use `object-fit:cover` only where justified by a fixed aspect ratio. The image must not produce overflow or distort the planet. No stars/animated effects.
5. **If you do not have the approved binary:** do not point live HTML at a missing asset. Still complete the source regression below and report binary upload as a genuine blocker with exact instructions to obtain the approved file. Do not invent a replacement or claim hero is done.

## B. Test Contact and all four papers

- Confirm Contact's actual rendered DOM uses v2 header/nav/footer and **no v1 old layout or active form**; the paused-enquiry status and LinkedIn work as read-only links.
- Confirm all four papers render the same six-link v2 navigation, clear long-form reading typography, fully justified paragraphs, readable figures and old article URL compatibility. The original seven figure `src` references per paper and every `<main>` content block must remain unchanged.
- Verify original scientific artwork/figure text is **not recertified** by the CSS redesign; provenance and scientific caution register remains outstanding. Don't change article mathematics casually.
- Audit `css/v2-articles.css` against legacy CSS specificity, mobile headings, tables, captions, long formula wraps, and dark contrast. Fix only documented presentation issues, without rewriting papers.
- Run updated `python3 docs/reports/scripts/v2_stage8_qa.py` from an actual feature-branch checkout. Check **320, 390, 768, 1440px**, HTTP/local references, complete catalogue counts, seven historical `noindex` pages, paused form, sitemap (16 locs), console/keyboard/menu.
- Capture **fresh Contact and Paper 1–4 desktop/mobile screenshots** and, after binary upload, homepage desktop/mobile screenshots. Do not reuse prior images as evidence of new changes.
- Save a report `docs/reports/V2_STAGE_08C_VISUAL_REGRESSION.md`, with verified successes, any blockers, new GitHub commit, explicit scope limitations and links to screenshots.

## Stop condition / handback

Continue in the **existing feature branch and draft PR #5**, commit genuine code, image files, test evidence and report as available. Finish with a concise **COPY TO CHAT**, listing what was actually completed and what remains.

**Never merge, deploy, mark ready, re-enable the enquiry form, restart lesson writing, reintroduce stars, or declare original figure rights and scientific correctness cleared.** Stage 9 release approval remains separate and explicit.

## DTSU v1.1

Read [the DTSU standard](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md). Use real UK-local clock, 0% before starting, factual progress at 10% milestones and within 3–5 minutes on lengthy work, and a truthful ETA in every visible update. Report 100%/ETA 0 only if this bounded work was validated; otherwise state the actual blocker.
