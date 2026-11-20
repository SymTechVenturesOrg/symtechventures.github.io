# Paper One — Seven owner-visually-approved cinematic PNG masters

**Current state:** `DIRECT_GITHUB_SHA256_VERIFIED`. All seven exact original PNG binaries were imported and independently read back from GitHub at commit c6f60ee180c2f5d401b0f597f512898c010981a9. The manifest preserves original byte lengths and SHA-256 values.

The owner approved all seven illustrations visually. Independent science/editorial QA is complete with findings; that does not make the artwork science-approved or authorised for website integration. Per-image dispositions and narrow recommendations are recorded in the [GitHub-native QA report](../../../reports/V2_PHASE_03_WORK_PAPER_ONE_SEVEN_GITHUB_NATIVE_INDEPENDENT_QA_20261120.md).

These are staged archival/review assets only. They are not active website images. Website HTML, production assets, PR #5, merge and deployment were not changed.

## Original identity and verification

The canonical manifest defines exact filenames, byte counts and source SHA-256 values. The staging bridge returned each original PNG as binary image content; source SHA-256, byte length, PNG signature and 1920×1080 dimensions were checked before upload. A fresh binary Git checkout at c6f60ee180c2f5d401b0f597f512898c010981a9 was then independently checked with sha256sum, file, Git tree object IDs and Pillow image decoding.

All seven readbacks match. From this commit onward, future QA inputs should come from pinned GitHub binaries rather than the temporary staging bridge.

## Owner-approved source identities

| Slot | File | Bytes | SHA-256 |
|---|---|---:|---|
| Cover | P1_Cover_OWNER_VISUALLY_APPROVED_1920x1080.png | 3089586 | 3eeba0f6bfcefd2a63b5867cad0442ac9a6d356526cc1fed31e057d3de9e95a8 |
| 1.1 | P1_Figure_1_1_OWNER_VISUALLY_APPROVED_1920x1080.png | 2972672 | 4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675 |
| 2.1 | P1_Figure_2_1_OWNER_VISUALLY_APPROVED_1920x1080.png | 3062802 | 446af968d82601de428bf719aef9c6a18c837d6b91626955edc04e14613f58e4 |
| 3.1 | P1_Figure_3_1_OWNER_VISUALLY_APPROVED_1920x1080.png | 3384953 | 62af2ce4790324056dff019c9d1617bd7c9d734b9a9201e40131a0329d1bc317 |
| 4.1 | P1_Figure_4_1_OWNER_VISUALLY_APPROVED_1920x1080.png | 3244273 | 788e68dc507c1e408428380b86816e594301384ed29331a3ab9aa9c29cdb9238 |
| 5.1 | P1_Figure_5_1_OWNER_VISUALLY_APPROVED_1920x1080.png | 3079962 | 945a5061c67bd52300cc4823f9664579380c85b36363daadcc7ef88496687b1c |
| 6.1 | P1_Figure_6_1_OWNER_VISUALLY_APPROVED_1920x1080.png | 3073681 | a1c9c939c6195a97106a3e4c8a49398a48b27baf108a8ef7b21bdc0ed09e896f |

The locked visual standard remains the style authority; the Paper One and Two references were used for style comparison only, not physics approval. Website integration remains unauthorised pending a separate handover.
