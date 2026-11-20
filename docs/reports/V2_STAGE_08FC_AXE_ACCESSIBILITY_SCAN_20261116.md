# Stage 8F-C axe Accessibility Scan

**Starting SHA:** `b0fac49`
**Branch:** `feature/v2-space-research-website` · [Draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)
**Outcome:** Automated scan blocked; no axe findings can be reported.

## Tool attempt

Local Node resolution found no `axe-core`, `@axe-core/playwright` or `pa11y`. One temporary install was attempted, without touching repository dependencies:

```sh
AUDIT_TMP=$(mktemp -d /tmp/axe-stage8fc.XXXXXX)
npm install --prefix "$AUDIT_TMP" --no-save --no-package-lock --ignore-scripts axe-core
```

Exit code **1**: `npm error code ENOENT`, `syscall mkdir`, path `/home/agent/.npm/_cacache`, errno `-2`. The environment could not create npm's configured cache directory. Per the bounded-retry instruction, no further installation attempts were made. No axe runtime/version or scan output exists; all 12 route/viewport scans and the Research open-menu scan are **BLOCKED**.

## Manual evidence carried forward

The prior Stage 8F-B report records six routes loaded in Chromium at 390 px and Research Escape-close/focus restoration. In this task, source inspection confirms the Research summary has an `aria-label="Open navigation menu"` and the navigation script sets Open/Close labels from `menu.open`. These are source observations, not a live-browser interaction result. This run did not independently execute outside-click, skip activation, desktop focus/current-page, or screen-reader checks. Therefore accessibility findings remain undetermined, not zero.

| Routes | 390 px | 1440 px | Research open-menu |
|---|---|---|---|
| Home, Research, BridgePoint, Discussion Papers, Contact, Paper 1 | BLOCKED (axe unavailable) | BLOCKED (axe unavailable) | BLOCKED (axe unavailable) |

No website source was changed; the integrated full regression was not repeated. No accessibility fix is claimed. The missing approved Earthrise asset, other asset provenance, and mathematical/scientific accuracy of paper figures remain separate owner/editorial decisions. Automated findings, contrast evaluation and screen-reader behavior remain unverified; this report is not a WCAG certification.

**Release status:** accessibility scan blocked, do not infer release readiness. PR remains draft; no merge or deployment occurred.

## 16 November recovery addendum — isolated-cache axe run

The authorised second attempt used an isolated temp cache and prefix:

```sh
AUDIT_TMP=$(mktemp -d /tmp/axe-stage8fc-recovery.XXXXXX)
mkdir -p "$AUDIT_TMP/npm-cache" "$AUDIT_TMP/pkg"
NPM_CONFIG_CACHE="$AUDIT_TMP/npm-cache" npm install --prefix "$AUDIT_TMP/pkg" --no-save --no-package-lock --ignore-scripts axe-core
```

Install exit code **0**, axe-core **4.14.1**. Python Playwright/system Chromium ran actual `axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa']}})` on all six specified routes at 390 and 1440 px (12 scans), plus live Research-menu interaction checks at 390 px. Browser runs used the local repository server.

| Routes | 390 px | 1440 px |
|---|---|---|
| Home, Research, BridgePoint, Discussion Papers, Contact | `label-content-name-mismatch`, serious, one `.brand` node on each route | Same, one `.brand` node on each route |
| Paper 1 | `label-content-name-mismatch`, serious, one `.brand`; `scrollable-region-focusable`, serious, one `table` | `label-content-name-mismatch`, serious, one `.brand` |

Research open-menu axe scan was **not run**. Real browser interactions observed: computed `aria-label` was Open before opening and Close after; Enter opened; Escape closed and returned focus to `SUMMARY`; outside click closed the menu. Full 8F-A regression was not repeated because website source did not change.

Findings are not silently fixed in this audit: brand accessible-label mismatch across all routes (remove/align `.brand` label with its visible text); mobile paper table lacks a keyboard-focusable scroll region (review a minimal `tabindex="0"`/accessible scroll treatment without altering paper content). No keyboard or screen-reader assessment beyond the specified interactions is claimed. These serious axe findings require correction and retest before accessibility sign-off. The temp package/cache were kept outside the repository and removed after the scan.
