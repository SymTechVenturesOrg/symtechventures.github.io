# Phase 2 — Interactive SYMMETRIA figure zoom (mouse wheel and pinch)

**Date:** 18 November 2026 GMT  
**Owner direction:** The existing opening of images into separate browser tabs is useful, but desktop readers should also zoom with the mouse wheel, in both directions; mobile users should retain landscape and pinch-to-zoom.
**Status:** Feature implemented on draft PR #5. Exact-source GitHub Actions QA awaiting final result; no merge or deployment.

## Design

Each of the four available papers still has seven original figures, with a clearly marked **Open interactive image viewer ↗** link. Opening a figure now launches a dedicated standalone viewer page (`pages/figure-viewer.html`) in a new browser tab, keeping the paper at its current place. The viewer uses the original unmodified WebP image from `images/symmetria/paper-01..04`.

The viewer provides wheel zoom anchored to the cursor, drag-to-pan, a mobile two-pointer pinch gesture, Fit, 100%, Zoom In/Out, keyboard +/-/0 and arrow panning when the stage is focused. The image viewer layout fills the available window in both portrait and landscape. A separate **Original image ↗** link remains available for raw WebP access. The original four HTML paper bodies, all 28 image binaries and figure captions are unmodified.

## Security / accessibility

The viewer allows only local image paths matching `images/symmetria/paper-0[1-4]/[A-Za-z0-9_-]+.webp`, rejecting arbitrary user-supplied URLs, and renders the alt description with `textContent`. All controls have accessible labels, keyboard focus, and mobile tap targets; the figure region is keyboard focusable. Invalid links show an error without making an external request. No third-party scripts or trackers. Source links use `rel=noopener`.

## Required validation

GitHub Actions must pass the full legacy v2 website regression and a dedicated 12-case matrix (4 available papers × desktop, mobile portrait and mobile landscape), confirming all 84 image-link renderings, popups to the new viewer, original file load, zoom buttons, actual wheel zoom in/out, pan, simulated two-pointer pinch and invalid-URL rejection. Real-phone pinch/orientation should also be tested by the owner.
