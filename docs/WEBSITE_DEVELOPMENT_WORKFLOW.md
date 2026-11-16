# Website Development Workflow — Chat, Work, Codex and GitHub

**Version:** 1.0 proposal  
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
| **Chat** | Agree objectives, editorial direction, priorities, scope and final acceptance with the project owner | Approved brief, decisions and review feedback | Claim final approval or bypass the review process |
| **Work** | Research and content preparation; assess factual/educational quality, accessibility, consistency and **real rendered previews** | Editorial source brief, lesson/research copy, evidence notes, content acceptance report | Compete with Codex on the same implementation files; publish or merge |
| **Codex** | Implement HTML/CSS/JS/data, maintain links and templates, fix browser/responsive issues, run repository and accessibility checks | Changes on a feature branch, draft PR, test log and screenshots from real renders | Change `main`, merge, deploy or rewrite research claims independently |
| **GitHub** | Source control, issues, pull requests, review history, reproducible code and publishing workflow | Versioned artefacts, PRs, deployment status | Automatically promote unapproved drafts to the website |
| **Project owner** | Accept research framing, approve content, approve design and approve merges | Explicit approval recorded in conversation/PR | N/A |

Roles describe an intended operating workflow, not promises that every environment supports the same browser, connector or automation features. Report actual tool access and verification truthfully.

## Standard sequence

1. **Chat scope:** agree audience, page outcome, content status, accessibility and existing URLs to preserve; create or link a GitHub Issue.
2. **Work editorial brief:** prepare accessible wording and citation provenance for scientific claims, including clear maturity labels.
3. **Codex implementation:** use a specific branch and a PR in the website repository; do not write to `main`.
4. **Codex technical checks:** validate HTML, navigation and internal URLs, mobile layouts, keyboard access, image alt text, semantic headings, sitemap, metadata and redirects/legacy paths.
5. **Work content/design checks:** inspect actual browser-rendered preview, not an AI-imagined screenshot; verify correct wording, mathematical notation, readability and distinction between evidence categories.
6. **Chat owner review:** present a real visual preview or state plainly why unavailable; collect corrections and explicit sign-off.
7. **Publish only after approval:** merge the agreed PR, verify the GitHub Pages deployment and recheck the live page. Never announce publication before success is confirmed.

## Parallelism and conflict avoidance

- Assign one implementation owner per file or PR. Work should not modify HTML/CSS files already assigned to Codex.
- Draft text in agreed content source files or the editorial brief; let Codex map approved text into the website.
- If research facts change, update the brief or source content first and request a targeted code correction.
- Separate architecture/content approval from merge/deployment approval.
- Keep the private `symtech-ventures` repo for internal programme work. Material crosses to this public repository only via a separate, reviewable publication decision.

## Scientific standards

- Make *established science*, *literature-derived interpretation*, *working hypothesis*, *simulation* and *experimental result* visibly distinct.
- Do not treat a mathematical toy model as empirical confirmation or propose physically implausible propulsion as tested technology.
- Source and check educational explanations, calculations, external quotations and diagrams.
- Display programme targets as **proposed** until evidence has been recorded.
- Discussions/essays accessible on the website are not automatically formal scientific publications.
- The **Publications** section stays empty until the owner explicitly authorises a qualifying publication.

## Dr T Style Updates (DTSU)

Provide concise timestamped work updates for multi-stage tasks: actual Europe/London time, defensible whole-task percentage, truthful results, blockers and an **estimated ETA** with uncertainty. Explain which scope the percentage measures. Record test/evidence links in the PR. Do not claim a future automated update unless it has been configured.

## Non-negotiable release gates

- No merge or publication without explicit owner authorisation.
- No accidental loss of existing articles or public URLs.
- No posting private scientific drafts, unpublished results, third-party materials or personal information without approval.
- A documentation/planning PR can be reviewed and merged separately from actual web-page implementation.
- Keep `main` and the current live website untouched until the approved production PR.
