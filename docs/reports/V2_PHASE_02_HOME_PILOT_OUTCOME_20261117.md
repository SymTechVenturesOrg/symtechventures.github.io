# Phase 2 — Homepage Hero Artwork Pilot: First Attempt

**Date:** 17 November 2026 (GMT)  
**Project:** SymTech Ventures v2.0  
**Source:** [Approved Phase 1 layout freeze](../V2_PHASE_01_LAYOUT_FREEZE_20261117.md), [Phase 2 design brief](V2_PHASE_02_SITE_ARTWORK_BRIEF_20261117.md)  
**Status:** **NOT APPROVED FOR WEBSITE — PILOT NEEDS VISUAL REFINEMENT**

## What was actually done

Phase 2 begins with the agreed **single homepage hero** slot in the existing `.orbit-wrap` container; no Research/BridgePoint images have been commissioned.

- Two initial AI image-generation attempts produced **off-brief status-dashboard compositions**, containing text and several imagery/quantity claims inconsistent with the artwork brief. They are **rejected** and will not be used or committed as production website assets. Do not treat their embedded checklist texts or image counts as project facts.
- As a fallback **technical/format prototype**, Chat generated an original, procedural Earth-above-lunar-horizon illustration without stars or typography. It was rendered in Python at **1432×988 PNG** and exported at **716×494 WebP** with encoder **quality value 80**, method 6.
- Measured local output sizes: source PNG **546,366 bytes**; WebP quality 80 **10,888 bytes**. The smaller WebP is largely a result of simple smooth shapes and does **not** show that visual image detail is sufficient.
- **Aesthetic evaluation:** this procedural output is **not polished enough to replace the existing orbital SVG**. Its purpose is to verify target size and WebP conversion settings, **not** obtain automatic final art approval.

The technical pilot files are available to the user in the active Chat conversation as generated attachments:
- `symtech_phase2_earthrise_pilot_source.png`
- `symtech_phase2_earthrise_pilot_q80.webp`

These local generated files are **not committed to the implementation GitHub branch** and should not be referenced in website HTML or used as live assets. There is no GitHub binary for them to link to.

## Next controlled art step

Obtain one **high-quality AI-rendered, text-free** Earthrise-style conceptual image that meets the actual restrained navy/cyan/amber design brief, with no starfield. The user must review it before Codex conversion/integration. A technical prototype showing WebP encoding is **not equivalent to approved artwork**.

Once the user chooses a suitable image, use Codex (Luna Medium / Standard) for deterministic WebP quality-80 export and *separate* PR #5 integration with full 320/390/768/1440 browser and regression verification. Current orbit SVG remains until then.

## Current state

**Phase 1 layout: owner-approved. Phase 2: design brief and first technical pilot complete, no approved raster image. Phase 3: not started.** No website source/paper figure changes, no merge and no deployment.
