# SYMMETRIA canonical cinematic anchors — independent GitHub object identity check

**Date:** 20 November 2026.  
**Source:** owner-provided `SYMMETRIA_Canonical_Cinematic_Style_References_20261120.zip`.  
**Branch:** `docs/symmetria-style-reference-assets-20261120`.  
**Outcome:** all 3 PNGs are present as GitHub Git blobs, with blob IDs exactly matching byte-for-byte computations from the owner-supplied originals. **Direct SHA-256 of GitHub-re-downloaded PNGs NOT done**, as the authenticated connector suppresses PNG bytes and its Git blob route rejects non-UTF-8 bytes.

| File | Source bytes | Original SHA-256 | Local-computed Git blob SHA-1 = GitHub reported blob SHA-1 |
|---|---:|---|---|
| `P1_Nilpotent_Operator_STYLE_ONLY.png` | 2109047 | `1cb364be9159452134594f3f7e86de5424d82c8738b209d7ebb8622b90e7d9f2` | `51831f2a286b7f7dc96524aeb15ca1855c804d52` |
| `P2_Noether_Conservation_STYLE_ONLY.png` | 2276356 | `1f7515074252b54bf4cbb6ef70683610e528c1f322097090751e1304a5f35593` | `19fca380f96c8e9ef4bd4a37d396b22658019631` |
| `P2_Broken_Symmetry_STYLE_ONLY.png` | 2232529 | `484191f41f002cc286938299da77de91b0dac14e8e9ef808ef356cb5b93e5817` | `9064d2a8dcdea6c5256dac690021adcf8e89b0a7` |

Checks: 3/3 ZIP-original PNG signature checks; 3/3 native dimensions 1672×941; 3/3 source SHA-256 checks against committed manifest; 3/3 `GitHub.fetch_file` path reads confirm expected blob SHA-1; GitHub asset bytes could not be retrieved by present connector. All are **STYLE ONLY**, not publication artwork, and must not be used as physics claims.

**Remaining:** for strict direct post-upload SHA-256 verification, use an authenticated binary-capable `git fetch` / `git show <commit>:<path>` or download-raw route in a linked Work cloud computer with repository access, and compare to the three manifest SHA-256 values. No merge, release or website changes are authorised by this report.
