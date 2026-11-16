# Stage 8F-B Focused Accessibility Assurance

**Branch:** `feature/v2-space-research-website`
**Starting SHA:** `ffe6b917bcc97d15f891e97c5ca393b3f36f8c24`
**PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)
**Verdict:** Automated scan BLOCKED; limited manual browser checks completed. No WCAG conformance claim.

## Automated check

Checked installed Node modules with `node -e "for(const p of ['axe-core','@axe-core/playwright','pa11y'])try{console.log(p,require.resolve(p))}catch{}"`; no scanner package was installed. A bounded local/offline availability check therefore found no axe/equivalent executable. No new dependency or external service was added. Automated accessibility audit is **BLOCKED**, not passed.

## Manual browser check

Used installed Python Playwright and `/usr/bin/chromium` headless against a local HTTP server. A real Chromium visit at 390 px loaded `/`, Research, BridgePoint, Discussion Papers, Contact and Paper 1 with titles and one skip link each; their local CSS, scripts and Paper 1 figures loaded successfully. On Research, the mobile disclosure opened, Escape closed it, and focus was on `SUMMARY` afterward. This short spot check did not test skip-link activation, outside-click dismissal, desktop current-page highlighting, contrast, target dimensions or screen-reader behavior. Menu accessible-name transition was not independently verified because summary text rendered as `Menu ☰` before and after click in this check; this should be followed up against the native disclosure state and current JS implementation.

| Route | 390 px browser load | 1440 px | Automated scan |
|---|---|---|---|
| Home | Visited | Not audited | Blocked |
| Research | Visited; menu Escape/focus spot check | Not audited | Blocked |
| BridgePoint | Visited | Not audited | Blocked |
| Discussion Papers | Visited | Not audited | Blocked |
| Contact | Visited | Not audited | Blocked |
| Paper 1 | Visited; styles and figures loaded | Not audited | Blocked |

No source change was made. Integrated regression was not rerun. Complex accessibility, contrast and screen-reader assessment remain open. Earthrise asset provenance and original figure accuracy are separate owner/editorial decisions.

PR remains draft; no merge or deployment occurred.
