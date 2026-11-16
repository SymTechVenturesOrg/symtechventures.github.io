# Website Development Workflow — Chat, Work, Codex and GitHub

**Version:** 1.1 proposal — Chat-led, token-efficient workflow  
**Date:** 16 November 2026  
**Status:** Review-only; does not authorise edits to production pages or publication  
**Site:** https://www.symtechventures.com/  
**Production repository:** `SymTechVenturesOrg/symtechventures.github.io` (public GitHub Pages)

## Purpose

Build and maintain a clear, accessible independent-research website focused primarily on **space exploration**, with careful separation of established science, exploratory theory, mathematical research, computer simulations and unvalidated concepts.

The website is not a start-up fundraising pitch, a claim of commercial technology, or a substitute for peer-reviewed research.

## Responsibility boundaries

| Role | Primary responsibility | Evidence/output | Must not do without explicit approval |
| --- | --- | --- | --- |
| **Chat** | **Continuous project lead and main execution environment:** source-grounded audit, research/document drafting, GitHub plans and Issues, decisions, reviews, DTSUs and owner-approved release coordination | Approved briefs, page copy, GitHub evidence and hand-off decisions | Claim final owner approval or bypass the review process |
| **Work** | **Intermittent editorial/visual specialist:** selective asset review, scientific/educational accuracy checks, the BridgePoint pilot and genuine render acceptance when supported | Short evidence-based reviews, checked copy and concise hand-backs | Compete with Codex on implementation files; publish or merge |
| **Codex** | **Intermittent engineering specialist:** desktop/mobile prototype, HTML/CSS/JS construction and final technical QA; owns implementation files during its stage | Feature-branch PR, reproducible tests and true browser screenshots | Change `main`, merge/deploy without authorisation, or rewrite research claims independently |
| **GitHub** | Source control, issues, pull requests, review history, reproducible code and publishing workflow | Versioned artefacts, PRs, deployment status | Automatically promote unapproved drafts to the website |
| **Project owner** | Accept research framing, approve content, approve design and approve merges | Explicit approval recorded in conversation/PR | N/A |

Roles describe an intended operating workflow, not promises that every environment supports the same browser, connector or automation features. Report actual tool access and verification truthfully.

## Chat-led, alternating specialist sequence

1. **Stage 1 — Chat only:** freeze the scope, four existing paper URLs, GitHub boundaries and review gates.
2. **Stage 2 — Chat + Work (Luna):** Chat inventories assets and content; Work contributes a bounded visual/editorial assessment.
3. **Stage 3 — Chat only:** prepare sitemap, programme outlines, page copy briefs and scientific-status rules.
4. **Stage 4 — Chat + Codex (Luna):** Chat supplies the approved design brief; Codex builds and renders one homepage prototype.
5. **Stage 5 — Chat + Work (Luna):** Chat drafts core copy; Work checks scientific accuracy, clarity and evidential wording.
6. **Stage 6 — Chat + Codex (Luna):** Codex implements the replacement site from approved content on its own feature branch/PR; Chat reviews and directs.
7. **Stage 7 — Chat + Work (Luna):** Work reviews one complete BridgePoint pilot lesson and remaining integrated content for correctness.
8. **Stage 8 — Chat + Codex (Luna):** Codex runs technical/accessibility/regression checks and completes targeted fixes.
9. **Stage 9 — Chat only by default:** Chat obtains a separate explicit owner approval, coordinates GitHub release and verifies live pages. Any specialist troubleshooting requires a new bounded request.

**Engagement order: Work → Codex → Work → Codex → Work → Codex.** There are three **planned** engagements of each. Do not run both specialists against the same files, keep open-ended tasks running or imply future/background progress without an actual scheduled workflow. The [revised nine-stage workplan](WEBSITE_V2_WORKPLAN.md) governs estimates and acceptance checkpoints.

## Parallelism and conflict avoidance

- **Chat remains the lead at every stage**, including the Work and Codex support stages. Assign one implementation owner per file or PR. Work must not modify Codex-owned HTML/CSS/JS.
- Chat drafts and reviews most text in agreed content sources or a bounded brief; Work is reserved for material scientific/educational checks. Codex maps approved copy into website templates.
- If research facts change, Chat updates the source brief or copy first and requests only a targeted code correction where needed. Do not launch another full Work review routinely.
- Separate architecture/content approval from merge/deployment approval.
- Keep the private `symtech-ventures` repo for internal programme work. Material crosses to this public repository only via a separate, reviewable publication decision.

## Scientific standards

- Make *established science*, *literature-derived interpretation*, *working hypothesis*, *simulation* and *experimental result* visibly distinct.
- Do not treat a mathematical toy model as empirical confirmation or propose physically implausible propulsion as tested technology.
- Source and check educational explanations, calculations, external quotations and diagrams.
- Display programme targets as **proposed** until evidence has been recorded.
- Discussions/essays accessible on the website are not automatically formal scientific publications.
- The **Publications** section stays empty until the owner explicitly authorises a qualifying publication.

## Token and model policy

- Prefer **Luna** in every Work and Codex engagement where model selection is offered; **Terra has no planned allocation**.
- Escalate to Terra only for a specific persistent failure, after narrowing the problem and obtaining the project owner's explicit approval.
- Chat cannot force the model picker or promise exact token costs; record actual model choice and relevant limits when known.
- Each specialist receives a short, bounded GitHub-linked brief with named files, expected evidence, acceptance criteria, exclusions, and a concise **COPY TO CHAT** handback.
- Chat performs routine drafting, GitHub metadata, documentation edits and reviews through available connected tools; do not duplicate work across all three modes.

## Dr T Style Updates (DTSU)

Provide concise timestamped work updates for multi-stage tasks: actual Europe/London time, defensible whole-task percentage, truthful results, blockers and an **estimated ETA** with uncertainty. Explain which scope the percentage measures. Record test/evidence links in the PR. Do not claim a future automated update unless it has been configured.

## Non-negotiable release gates

- No merge or publication without explicit owner authorisation.
- No accidental loss of existing articles or public URLs.
- No posting private scientific drafts, unpublished results, third-party materials or personal information without approval.
- A documentation/planning PR can be reviewed and merged separately from actual web-page implementation.
- Keep `main` and the current live website untouched until the approved production PR.
