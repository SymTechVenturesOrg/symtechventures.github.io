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

- [ ] Owner confirms the origins and right to display/reuse the **six common legacy logos** and **28 paper-specific illustrations** (34 known distinct images), recording AI-generated, self-created, commissioned/licensed or external-source exceptions.
- [ ] Review **other retained historical-page and CSS image assets**; `noindex` does not mean inaccessible.
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

- [ ] Read versioned `docs/reports/V2_STAGE_08C_ASSET_PROVENANCE_REGISTER.md`, if created by Codex, and reconcile it against the existing Stage 9 register rather than assuming duplicated inventories agree.
- [ ] Read `docs/reports/V2_STAGE_08C_PRE_RELEASE_ASSURANCE.md`, exact tested commit SHA and all attached genuine screenshot evidence.
- [ ] Verify automated accessibility tool used and actual results, plus manual keyboard/menu/landmark/focus/alt/contrast caveats; **no implied full WCAG certification**.
- [ ] Review Open Graph and social-preview updates; share image only where rights and factual suitability are cleared.
- [ ] Confirm exact-branch `python3 docs/reports/scripts/v2_stage8_qa.py` run and exit code after all implementation changes.
- [ ] Check HTTP/resource errors, links, sitemap, `CNAME`, preserved paper URLs and bodies/figures, mobile widths 320/390/768/1440px, and any unresolved performance issues.
- [ ] Verify the implementation PR is **still open, draft and unmerged** before the owner authorises anything.

## E. Owner acceptance questions

Record answers or explicit defer/resolve decisions in the release review, not as assumptions:

1. **Images:** Were the original paper figures and shared logos personally created, commissioned, AI-generated or obtained elsewhere? If mixed, which exceptions?
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

- Stage 8B regression was reported passed, but significant **later** Contact/article-shell changes require new exact-branch tests.
- Owner-approved privacy/noindex controls are implemented on the **unmerged** development branch.
- A previous screenshot/issue report states the proposed Earthrise WebP file was not yet in GitHub.
- The existing illustration register includes preliminary checks on **two** figures and does **not** constitute mathematical or rights clearance.
- **Stage 8C Codex report is not yet available at checklist preparation.** The owner has dispatched its handover; there is no basis to assume completion.
- PR #2 and PR #5 are separate drafts; do not merge the planning PR as part of a website release unless separately authorised.

**Stage 9 status: prepared for review, NOT approved to release.**
