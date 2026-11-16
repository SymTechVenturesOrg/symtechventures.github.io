# SymTech Ventures v2.0 — Stage 6A: Implement Homepage Shell

**Task:** Complete only the first implementation checkpoint of Stage 6. **No merge or deployment.**

**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Parent task:** [Stage 6 full-site requirements](V2_STAGE_06_CODEX_SITE_BUILD.md)  
**Tracker:** [Issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)

## Confirm work state first

The previous attempt reported a **local branch** named `feature/v2-space-research-website`, based on `main` commit `248feb5084745ebcffca5957ca5c517baa8ba7e0`, but no implementation, commits or PR.

At handover preparation, GitHub branch search did **not** find that branch remotely. Check the current working tree, local branch, remote and permissions. If the branch exists locally and is unchanged, **reuse it**; do not create a redundant branch. Fetch `main` and inspect changes before coding. If you cannot commit or push, provide the exact command/error and a concise blocker report — don't claim a PR exists.

## Read these source files

- [Approved homepage design prototype](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/prototype/space-first-homepage-20261116/prototypes/v2-homepage/index.html)
- [Approved information architecture and starfield requirements](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_STAGE_03_INFORMATION_ARCHITECTURE.md)
- [Website copy candidate](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/editorial/V2_STAGE_05_WEBSITE_COPY_DRAFT.md)
- [Stage 2 asset audit](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/reports/V2_STAGE_02_ASSET_AUDIT_20261116.md)
- [DTSU standard](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md)

## Implement **only** these items

1. Replace the root homepage **on your unmerged feature branch only**, adapting the approved Stage 4 prototype with independent research, primarily space-exploration focus and the four programme cards (SYMMETRIA, BridgePoint, NSRP, SEIP).
2. Extract reusable site styling/navigation/footer into small maintainable CSS/HTML/JS files as appropriate; don't redesign the approved visual direction.
3. Retain the **site-wide dark starfield visual identity**. On the homepage, use a restrained effect that respects `prefers-reduced-motion`, is decorative/non-interactive and does not obscure text. A simple working implementation is preferable to elaborate animation.
4. Include six approved navigation labels: Home, Research, BridgePoint, Discussion Papers, Publications, About. Their eventual real paths are defined in the parent brief; **clearly record links to pages not yet built** as pending Stage 6B, not passing link checks.
5. Preserve four original SYMMETRIA discussion-paper URLs from `/articles/symmetria/symmetria-paper-01.html` through `-04.html`. Display them as **online discussion papers**, distinct from formal Publications.
6. Keep the Publications catalogue empty, include the supplied LinkedIn URL, and avoid start-up marketing or claims of verified new physics.
7. Leave the original four paper HTML files, paper images, `CNAME`, enquiry/contact forms, legacy pages and existing deployment configuration unchanged.

**Do not build the Research, BridgePoint, NSRP, SEIP, About or Publications pages yet.** They belong to later Stage 6 checkpoints. Do not invent article/lesson content.

## Verify and hand back

- Run a real local browser check of the new root homepage at desktop (~1440px) and mobile (390px and 320px), checking overflow, headings, menu/focus and console errors.
- Verify four original article links and original article file hashes remain unchanged.
- Record which six nav destinations are **pending future implementation**; do not claim all site links pass yet.
- Commit and push the actual homepage work to the existing feature branch, then **open or update one draft PR against `main`**. If remote push/PR creation is blocked, give the exact failing operation and error; preserve the local work.
- Finish with a concise **COPY TO CHAT**: branch, commit, PR URL if it exists, changed files, actual test evidence and remaining Stage 6B tasks. Then stop.

## Visible DTSU v1.1

Read the linked standard before actions. Start with a clock-verified `[HH:MM:SS] 0% — factual status; ETA ~remaining duration.` and continue with truthful whole-task milestones (ideally every 10%; at least 10–20% when rapid), plus an update every 3–5 minutes on longer work. Every update must include an ETA, or `ETA unknown` if genuinely unpredictable. Only report **100% / ETA 0 minutes** once this **Stage 6A** implementation, checks and handback are actually complete.

**Stop after Stage 6A. Do not merge, deploy or begin Stage 6B autonomously.**
