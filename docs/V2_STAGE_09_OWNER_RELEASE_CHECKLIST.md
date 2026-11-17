# SymTech Ventures v2.0 — Stage 9 Owner Review and Release Checklist

**Prepared:** 16 November 2026 (GMT)  
**Status:** Review checklist only — **not a release approval**  
**Role:** Chat-led owner acceptance, separate from the active Codex Stage 8C technical assurance  
**Planning branch:** `planning/space-first-research-website-20261116` ([draft PR #2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2))  
**Implementation:** `feature/v2-space-research-website` ([draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5))  
**Website:** https://www.symtechventures.com/  
**Tracking:** [issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)

## Purpose and workflow boundaries

This is the **owner's Stage 9 acceptance and release gate**, not a task for Codex to deploy. The Codex Stage 8C assignment is still separate: provenance inventory, automated accessibility, SEO/share previews and final exact-branch browser regression. **Do not mark those pending checks as complete until an actual Codex report and readback exist.**

The owner sets the Codex model, thinking effort and speed **outside Codex**. Neither Chat nor Codex chooses or changes those settings.

**No commits to `main`, PR merges, deployment, DNS modifications or publication are authorised by this document or by a passing test.** A fresh and explicit owner instruction is required after the full checklist is reviewed.

## A. Known approved website requirements

| Requirement | What to verify at release | Acceptance |
| --- | --- | --- |
| Identity | Independent exploratory research project focused primarily on space exploration, not an operating deep-tech laboratory or Silicon Valley startup | Owner reviews current desktop and mobile appearance |
| Visual design | Restrained dark research identity; **no starfield** (newer owner preference overrides old Stage 4 instruction); fully justified *running prose*, naturally aligned headings/navigation | Fresh captures and owner approval |
| Main navigation | Home, Research, BridgePoint, Discussion Papers, Publications, About; Contact reachable in About/footer | All resolve, including on 390px mobile |
| SYMMETRIA | Original four discussion-paper paths/content/figures remain accessible; twelve later papers remain Planned | Body/figure preservation evidence |
| NSRP | Five research projects, four phases each, **20 planned phases** | Catalogue/check script |
| SEIP | Five engineering projects, four phases each, **20 planned phases** | Catalogue/check script |
| BridgePoint | Four groups, **16 Planned** lesson titles; no lesson links or pilot lesson published | Catalogue/check script |
| Publications | **Zero** formal publication records; online discussion essays are not mislabelled as peer reviewed | Read original page and metadata |
| Old pages | Seven historical division/fellow URLs retain informative history notice and `noindex,follow`; not in 16-location sitemap | Source and browser checks |
| Privacy | Contact and Enquiry clearly state submissions are paused, no working third-party form or personal-data transmission; former confirmation is truthful | Inspection only; no live submissions |
| LinkedIn | Owner's supplied public professional profile is present, not represented as a guaranteed messaging method | Link verified as far as environment permits |

## B. Asset provenance — hard release gate

Use the existing [Stage 9 image provenance register](reports/V2_STAGE_09_IMAGE_PROVENANCE_REGISTER.md), plus the Codex Stage 8C complete inventory when handed back.

- [x] **Creation method attested by owner:** The original **six shared logos and 28 SYMMETRIA paper illustrations** were generated using ChatGPT ("Synthman") under the owner's direction on 16 November 2026. See [owner provenance statement](reports/V2_STAGE_09_OWNER_AI_ARTWORK_PROVENANCE_20261116.md). This is a group-level owner attestation, not an independent file-by-file audit or legal licence certification.
- [ ] Confirm whether any third-party elements, external source images or licensing/attribution exceptions were incorporated in those 34 AI-generated assets; record material exceptions if any.
- [ ] Review **the other 12 historical image assets** (banners, icons and hero artwork) identified in Codex's 46-asset Stage 8C inventory. Their creation source was not explicitly confirmed in the owner's answer; `noindex` does not make them inaccessible.
- [ ] Record any author/source, applicable licence restrictions, attribution requirements and proof. **GitHub presence or earlier publication alone is not permission.**
- [ ] Resolve any unknown-rights materials by demonstrating permission, replacing/removing after separate owner approval, or deferring release. Do not claim a blanket clearance without evidence.
- [ ] If the new **Earthrise** homepage WebP is intended for launch, verify that the *actual* binary is in the implementation repository at the expected path, that its origin/rights and description are documented, and that desktop/mobile screenshots reflect the **committed version**. Earlier reports say a local PNG/WebP existed but was **not yet uploaded**; do not assume its presence or accept an HTML reference to a nonexistent file.

## C. Scientific-figure accuracy — separate hard editorial gate

Rights to an illustration **do not prove** the accuracy of equations or physics assertions within it.

- [ ] Inspect the full **28-figure set**, with substantive claim-bearing figures identified and assessed; record visual claims, source/derivation, caveats and pass/revise decisions. The existing register only documents two preliminary figure spot-checks; 26 remain unchecked there.
- [ ] **Paper 2** `02_noether_symmetry_conservation.webp`: blanket mirror/parity and time-reversal invariance is too broad. Weak interactions violate parity, and T violations are observed. Discrete P/T transformations are not equivalent to continuous Noether symmetries. Decide on a corrected graphic or carefully adjacent explicit qualification before public educational use.
- [ ] **Paper 3** `03_dirac_nilpotent_structure.webp`: distinguish a *conceptual* comparison of the Dirac equation with `N²=0` from a demonstrated mathematical equivalence. Supply a precise sourced derivation or qualify the graphic's claim.
- [ ] Any correction to scientific images or research text receives a **separate owner-approved, narrow editorial change** and fresh integrity baseline. Do not silently change protected original paper bodies or figures.
- [ ] Do not claim a peer review or experimental validation of SYMMETRIA by completing artwork checks.

## D. Codex Stage 8C evidence — pending until report handback

- [x] Read and reconciled Codex's `docs/reports/V2_STAGE_08C_ASSET_PROVENANCE_REGISTER.md` with the earlier Stage 9 inventory: 46 distinct referenced raster assets = 28 paper illustrations + six shared logos + 12 historical images. A creation source is now owner-attested for the first 34, not for the remaining 12.
- [x] Read `docs/reports/V2_STAGE_08C_PRE_RELEASE_ASSURANCE.md` and verified PR head `8e34f39529ceafa824e710ab827c3cbc748c8c24` in GitHub. The report documents real Contact and Papers 1–4 screenshots at 390/1440px; independently visual review the captures before final owner approval.
- [x] **Stage 8E targeted navigation improvement:** [source and Chromium component evidence](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08E_MOBILE_NAVIGATION_ACCESSIBILITY_20261116.md) confirms current-page link semantics, visible active-page styling, mobile open/close labels, Escape/focus handling and outside-tap dismissal. Focused smoke tests passed at 320/390/768/1440 px; **not** a full-site regression.
- [x] **Targeted automated accessibility scanner ran after fixes.** [Stage 8F-D report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08FD_ACCESSIBILITY_FIX_RETEST_20261116.md) records **axe-core 4.14.1 zero violations in 12 scans** (six routes at 390 and 1440 px) after correcting the branding accessible-name and horizontal-scroll focusability issues. The post-change exact-branch regression also exited **0**. This is a sampled rule scan, **not WCAG certification or screen-reader evidence**; do not infer that remaining manual accessibility checks passed.
- [x] **Paper 1 mobile table keyboard scrolling verified (Stage 8F-E).** In a real Chromium/Playwright run at 390×844, the focused table had a visible outline and its own `scrollLeft` moved **0 → 40 → 42 → 2** on ArrowRight/ArrowRight/ArrowLeft; the page did not scroll horizontally. At 1440×900 the table had no horizontal overflow or additional `tabindex`. Research mobile Open → Close → Open labels, Escape/focus return and outside-click dismissal also passed. [Read the committed Stage 8F-E report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08FE_KEYBOARD_TABLE_SCROLL_VERIFICATION_20261117.md). No site code was changed, so the prior Stage 8F-D **12 axe scans (zero findings)** and full-regression **exit 0** were not rerun. **Limits:** Papers 2–4 were not separately checked for table keyboard scrolling, and full screen-reader / WCAG certification remains unperformed.
- [x] **Stage 8D source verification:** [ten main pages now have text-only Open Graph and Twitter/X summary metadata](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08D_SOCIAL_METADATA_SOURCE_QA_20261116.md), with titles/descriptions/canonicals matched and all non-head page content unchanged. No new `og:image` was added. This is source-level QA, not an external social crawler preview.
- [ ] After any future Earthrise/share-image integration, confirm asset origin/rights, review actual share-card rendering, and rerun relevant browser checks.
- [x] Codex's Stage 8C report records exact-branch `python3 docs/reports/scripts/v2_stage8_qa.py` exit 0 after test-script fixes. Chat verified the committed report, not a second independent execution. Re-run if later image/site edits are made.
- [x] **Stage 8F-A browser regression evidence:** [source-verified Codex report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08FA_INTEGRATED_REGRESSION_20261116.md) recorded exit 0, links/resources, 16-location sitemap, preserved original four paper bodies/figures, programme counts, no console errors and mobile/desktop widths 320/390/768/1440px. Chat verified the report and commit in GitHub, not a separate independent browser run.
- [ ] Review actual performance measurements if launch policy requires them; no Lighthouse/Core Web Vitals test has been documented.
- [x] Verified PR #5 open, draft, unmerged at the Stage 8C reported commit; check this again immediately before any separate release approval.

## E. Owner acceptance questions

Record answers or explicit defer/resolve decisions in the release review, not as assumptions:

1. **Images:** The owner confirmed the original paper figures and shared logos were generated with ChatGPT. Are there **any third-party visual elements or exceptions**, and were the remaining 12 historical assets generated the same way?
2. **Mathematical illustrations:** Are the displayed figures intended as conceptual artwork or authoritative mathematical/physics explanations? Which claim-bearing graphics should be corrected, footnoted or replaced?
3. **Earthrise homepage visual:** Keep the current existing orbital SVG, or release with the proposed raster Earthrise graphic **if committed, verified and rights-cleared**?
4. **Overall appearance:** Does the final site at 390 and 1440 px match the approved no-starfield, justified, restrained research identity?
5. **Release:** After all blocking requirements are resolved, does the owner **explicitly approve merging PR #5 to `main` and triggering publication**? A generic “looks good”, permission to test, or approval of another PR is *not* sufficient.

## F. Release procedure — only *after* the owner explicitly approves

The following is a proposed runbook, **not an instruction to execute now**:

1. Read the latest exact feature PR head and `main` head SHAs, record CI status, review branch diff, and check there are no unexpected changes or merge conflicts.
2. Ensure every P1 rights, scientific-figure, privacy, security and accessibility blocker has either been resolved with evidence or given an explicit **informed owner decision** consistent with legal and safety requirements. An owner cannot manufacture permission to use third-party copyrighted material.
3. Obtain the owner's **new, explicit instruction** to merge/deploy the named PR/commit; do not infer from prior approval to prepare or run tests.
4. After authorised merge, verify GitHub Pages build/deployment status and production HTTPS content at the existing domain; do not claim success based only on a GitHub merge result.
5. Check key live pages at desktop and mobile, original Papers 1–4, navigation, Contact/Enquiry state, sitemap and `robots.txt`; check live URLs rather than assuming local tests transfer.
6. If a severe regression occurs, preserve evidence, report it promptly and seek owner approval for the appropriate rollback/revert. Avoid ad hoc DNS changes or destructive changes to the legacy pages. Record the before-release `main` SHA and reversal method in the release report.
7. Publish a final Stage 9 release verification report and a concise COPY TO CHAT handback, including actual live checks, outstanding nonblocking caveats and exact version/commit.

## Decision table

| Outcome | Meaning | Next move |
| --- | --- | --- |
| **Hold — pending evidence** | Stage 8C not back, assets or figures unreviewed, missing image binary, or a blocking test incomplete | Continue review; **no merge** |
| **Hold — material defect** | Broken links, inaccessible primary interaction, privacy regression, unknown image rights or misleading major scientific claim | Focused fix, retest, and owner review |
| **Ready for owner decision** | Required evidence complete, substantive blockers resolved, final visual/content acceptance recorded | Ask **specifically** for permission to merge PR #5 |
| **Released and verified** | Explicit approval + actual merge/deployment + independent live-page checks | Record verifiable final outcome |

## Current status when this checklist was prepared

- Stage 8B passed, and **Stage 8C Codex regression also passed** at commit `8e34f39529ceafa824e710ab827c3cbc748c8c24`; the [Stage 8C assurance report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08C_PRE_RELEASE_ASSURANCE.md) still rates the implementation **Pass with owner blockers; not release-ready**.
- Owner-approved privacy/noindex controls are implemented on the **unmerged** development branch.
- A previous screenshot/issue report states the proposed Earthrise WebP file was not yet in GitHub.
- The existing illustration register includes preliminary checks on **two** figures. The owner has now attested that the original paper artwork and logos were ChatGPT-generated, but their **scientific claims still require editorial checking**; the other historical images and any third-party-content exceptions remain to be confirmed.
- **Stage 8C Codex report is now available and source-verified**, including tests passed and missing automated accessibility evidence. The owner must decide whether to run a separate axe/equivalent or screen-reader check before release.
- PR #2 and PR #5 are separate drafts; do not merge the planning PR as part of a website release unless separately authorised.

**Stages 8F-A / 8F-B:** Stage 8F-A integrated regression passed at `db3a92d92d327ded3a83e020495ea99261ca8ad4`. Stage 8F-B committed at `336b14b9442010d546e6f032185987de83e5376d`: **automated accessibility BLOCKED**, with limited 390 px manual browser coverage. The outstanding audit must not be described as passing, and the site is not release-ready on the strength of these checks alone.

**Stage 8F-C historical finding (now retested):** [8F-C report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08FC_AXE_ACCESSIBILITY_SCAN_20261116.md) recorded two serious axe issues: branded accessible-name mismatch and unfocusable scrolling paper table. These triggered the 8F-D corrections; this paragraph is historical, not an indication the original axe violations remain open.

**Stage 8F-D correction:** [Verified GitHub report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08FD_ACCESSIBILITY_FIX_RETEST_20261116.md) records removing overriding brand labels on ten primary page headers and four paper shells, conditional `tabindex=0` on overflow tables, focus CSS, **12 axe scans with zero violations**, and `python3 -u docs/reports/scripts/v2_stage8_qa.py` **exit 0**. The GitHub diff shows original paper content remained protected.

**Stage 8F-E verification complete:** [Report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08FE_KEYBOARD_TABLE_SCROLL_VERIFICATION_20261117.md) confirms actual 390px Paper 1 table scrolling using ArrowRight/ArrowLeft, keyboard focus, 1440px non-overflow, and Research mobile-menu behaviour. At `77f82a0f9169978db6d6996ce5b0160c34da2e01`, the only newly committed file was the report. **Accessibility sampled technical tests pass; no full screen-reader test, WCAG certification, merge, deployment or release approval.**

**Stage 9 status: prepared for review, NOT approved to release.**
