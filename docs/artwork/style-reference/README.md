# SYMMETRIA — canonical cinematic AI style reference registry

**Status (20 November 2026): THREE PNG ORIGINALS PRESENT IN GITHUB — GIT BLOB IDENTITY CHECKS PASS (3/3). Direct SHA-256 recomputation from downloaded GitHub bytes remains BLOCKED by the connector.** The GitHub file-content route exposes correct blob SHA-1 IDs but returns no binary payload; the Git blob fetch route fails on PNG UTF-8 decoding. This is a transport limitation, not missing source images. This registry does not claim that the strict direct GitHub binary SHA-256 check passed.

This branch deliberately stores **reference artwork outside website/public image paths**. It must never be treated as a publication artwork source or physics authority. The three selected originals come from the owner's earlier visually approved Paper One/Two design family and encode only style: navy space-science background, richly luminous cyan/gold dimensional physics diagrams, gold serif subject titles, integrated explanatory labels, readable panel hierarchy, and optional bottom progression strip. **Source equation/text content may be wrong** and must never be copied unverified.

Originals: 1672 × 941. All *new final figures* must still be **1920 × 1080 exactly (16:9)**, independent full-canvas images. Do not upscale these sources into replacement figures.

## Verified uploaded immutable file set

| GitHub file | Source style origin | Original SHA-256 |
|---|---|---|
| `P1_Nilpotent_Operator_STYLE_ONLY.png` | Paper One | `1cb364be9159452134594f3f7e86de5424d82c8738b209d7ebb8622b90e7d9f2` |
| `P2_Noether_Conservation_STYLE_ONLY.png` | Paper Two | `1f7515074252b54bf4cbb6ef70683610e528c1f322097090751e1304a5f35593` |
| `P2_Broken_Symmetry_STYLE_ONLY.png` | Paper Two | `484191f41f002cc286938299da77de91b0dac14e8e9ef808ef356cb5b93e5817` |

Use `manifest.json` to check native dimensions, exact source sizes and hash identity. A style prompt must cite **at least two of these** as image references; no unrelated generator, scripted flat infographic, generic science collage or multiple-figure montage qualifies. If original bytes cannot be verified, mark **BLOCKED**. Owner must expressly approve style fidelity of the first regenerated image before wider batches. Scientific correctness is a separate QA gate.

For governance see the existing draft docs PR #6 and the mandatory locked cinematic standard. **Do not merge or deploy PRs based on this registry.**


## Independent post-upload identity check (20 November 2026)

Each SHA-256 below was recalculated from the exact original ZIP bytes; the Git blob SHA-1 was independently calculated as `SHA1("blob " + byte_length + NUL + original_file_bytes)`, then compared against the GitHub connector's SHA for that same branch path. This strongly corroborates byte identity but is **not** a direct SHA-256 recalculation on GitHub-downloaded bytes.

| Reference | GitHub blob SHA-1 | ZIP-computed blob SHA-1 | Check |
|---|---|---|---|
| `P1_Nilpotent_Operator_STYLE_ONLY.png` | `51831f2a286b7f7dc96524aeb15ca1855c804d52` | `51831f2a286b7f7dc96524aeb15ca1855c804d52` | MATCH |
| `P2_Noether_Conservation_STYLE_ONLY.png` | `19fca380f96c8e9ef4bd4a37d396b22658019631` | `19fca380f96c8e9ef4bd4a37d396b22658019631` | MATCH |
| `P2_Broken_Symmetry_STYLE_ONLY.png` | `9064d2a8dcdea6c5256dac690021adcf8e89b0a7` | `9064d2a8dcdea6c5256dac690021adcf8e89b0a7` | MATCH |

**Outstanding gate:** only label `DIRECT_GITHUB_SHA256_VERIFIED` after using an authenticated binary-capable GitHub download or local Git checkout to retrieve each committed PNG and recompute the SHA-256 from those retrieved bytes. Until then: uploaded and Git-object identity checked; direct SHA-256 readback pending.
