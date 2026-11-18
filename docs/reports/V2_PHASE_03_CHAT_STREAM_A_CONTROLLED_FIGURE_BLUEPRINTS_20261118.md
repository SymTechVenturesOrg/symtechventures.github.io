# Phase 3 — Chat Stream A: Controlled Scientific Figure Blueprints

**18 November 2026 GMT** · **State: candidate designs and figure text ONLY — no image files or paper source modified**  
**Pinned inspected website baseline:** `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f` (`feature/v2-space-research-website`)  
**Owner gate:** Approval of each proposed figure or caption change is still required. Do **not** treat this as image generation, scientific endorsement, merge approval or deployment instruction.  
**Related documents:** [source and figure ledger](V2_PHASE_03_CHAT_STREAM_A_FIGURE_LEDGER_AND_CORRECTION_BRIEF_20261118.md) · [Chat/Work parallel plan](../V2_PHASE_03_CHAT_WORK_PARALLEL_WORKPLAN_20261118.md) · [Work's independent 28-figure report, supplied in owner's Work conversation] (not copied into the public repository).

## 1. Inspection and design principles

Chat visually opened the original full-resolution WebPs corresponding to P1 Figs **3.1** and **5.1**, P2 Fig **4.1**, P3 Fig **4.1** and the four candidate P3 swap targets (Figs **1.1/3.1** and **5.1/6.1**), plus P4 Fig **4.1**, from the pinned GitHub source. Their actual embedded text and illustrative themes were checked against the adjacent HTML paper captions. Work's independently produced audit, inspected after the visual pass, agrees with the three original priority claim issues and flags **five high**, **14 medium** and **nine low** severity figures.

**Three design rules for every approved replacement:**

1. The public papers remain accessible **reference-free exploratory discussions**, influenced by Dr Peter Rowlands' nilpotent approach. A correct algebraic identity must not be made to imply an experimentally confirmed universe-wide mechanism; a named literature formulation must not be rebranded as independent SYMMETRIA validation.
2. The **graphic itself** must say what is known/assumed/proposed, because our new standalone full-size figure viewer may display it without the paper caption. Do not rely on an HTML caveat alone to correct an unequivocally false embedded claim.
3. Use **controlled, editable mathematical and label text** (SVG, authored text/vector overlay, or deterministic composition) alongside restrained artwork. Do **not** trust generated pixels to spell equations correctly. Before substitution compare source, output, 100%-size zoom and mobile/landscape legibility. Keep original WebP bytes and hashes.

### Shared visual architecture (proposed)

- Retain the professional dark navy/black scientific palette, gold or cyan accent keys and restrained cosmic motifs, **without** decorative equations that imply an actual derived model.
- Prefer a **three-panel story**: **Established/defined** → **specific mathematical idea** → **proposed questions and test criteria**. Use deliberate arrows only where the implication is justified, not visual arrows that falsely imply an established derivation.
- Clearly identify content status in the graphic with real words such as **Established physics**, **Specified algebraic construction**, **Hypothesis**, **Unresolved question**, **Must be tested**; avoid decorative badges or labels such as **Proven** for exploratory claims.
- Target the existing figure's orientation and source dimensions unless the owner approves a different crop. Aim at 1536 px class desktop source artwork and test readability at actual 390px page width and in the zoom viewer; don't squeeze long paragraphs into the raster.
- Replace only selected approved source references with versioned filenames (for example `01_symmetria_perspective_scientifically_revised_v2.webp`), never destroy the original asset. Keep explicit alt and the original viewer link functioning.

## 2. Blueprint A — Paper 1 Figure 5.1

**Source file:** `images/symmetria/paper-01/01_symmetria_perspective.webp`; original blob SHA `b0334e5aa0c42dd0463b3810689502f43fae680b`.  
**Actual source observation:** The **NILPOTENT FOUNDATIONS** panel displays `N² = 0` and `NA + AN = 0` together, with no definition of A. Other panels read like established emergence and fundamental consciousness claims, despite the bottom strip calling SYMMETRIA exploratory.

**Proposed revised title:** **SYMMETRIA: A PROPOSED RESEARCH PERSPECTIVE**.

| Panel | Exact approved-candidate label/copy | Visual direction |
| --- | --- | --- |
| 1 — Established algebra | **Nilpotence:** `N ≠ 0` and `N² = 0` *within a specified algebra*. | Typed equation in a clean outline frame, no second operator statement implying it follows |
| 2 — Distinct extra property | **Anticommutation:** For specially defined operators A and N, `AN + NA = 0` **may be imposed or derived separately**; it does not follow from nilpotence alone. | Separate small panel with a gap, not a consequence arrow; optional simplest approach is **omit this panel altogether** |
| 3 — Exploratory interpretation | **SYMMETRIA asks:** Could specified symmetry, algebraic constraints and information relationships help organise physical descriptions? | Conceptual network labelled **Hypothesis — not established physics** |
| 4 — What would count as progress | **Open tests:** define the algebra; recover established physical results; make quantitative, falsifiable predictions; compare with evidence. | Four clear process stages without future result claim |

**Must remove/qualify from old image:** "Nilpotent balance underlies nature", "self-cancelling structures create stability", "information meets the right constraints → meaning" and "all physical phenomena emerge" should not appear as unqualified conclusions; consciousness, if retained, must be explicitly speculative and preferably omitted from this concise physics figure.

**Mathematical QA example (for internal proof only, not required on the finished graphic):** `N=[[0,1],[0,0]]`, `A=I`; `N²=0` yet `AN+NA=2N≠0`. So an unconditional implication is invalid over the usual non-characteristic-two fields. If the anticommutator statement is omitted entirely, it eliminates the need to explain a special A inside a small illustration.

**Preferred owner decision:** controlled redraw/recomposition of the inaccurate panel(s) with the above copy; avoid a blanket artistic redesign of all other paper figures.

## 3. Blueprint B — Paper 2 Figure 4.1

**Source:** `images/symmetria/paper-02/02_noether_symmetry_conservation.webp`, SHA `66d7ba1ca508f4f54457e922a5b5fdc1085ca9f4`.  
**Actual observation:** The illustration has independent panels claiming **all laws are the same in mirror-image situations** and whether time runs forwards/backwards. Its Noether table maps `Gauge Symmetry` directly to charge conservation without clarifying the global/local distinction. It also implies symmetry alone "predicts particles".

**Proposed title:** **CONTINUOUS SYMMETRIES, CONSERVATION AND LIMITS**.

| Panel | Controlled wording | Scientific condition |
| --- | --- | --- |
| A — Continuous spacetime symmetries | **Time translations → energy conservation**; **Space translations → momentum conservation**; **Continuous rotations → angular momentum conservation**. | Under the relevant conditions, continuous symmetries of the action yield conserved Noether currents/charges. Do not imply symmetries persist if external backgrounds or time-dependent dynamics break them |
| B — Phase and gauge | **Global phase symmetry → conserved charge (under the specified assumptions)**. A local gauge transformation is a **redundancy of description**, not an independently conserved physical charge for each arbitrary local transformation. | Avoid saying local gauge invariance itself automatically creates a new physical global conservation law |
| C — Discrete transformations | **Parity P:** weak interactions can violate mirror symmetry. **Time reversal T:** certain particle processes violate T symmetry. | Do not portray P/T as universally exact invariances or conflate these discrete symmetries with Noether's first theorem |
| D — Research meaning | **Symmetry guides model-building and constrains predictions; experiments determine which symmetries nature respects.** | No direct "symmetry alone predicts any particular particle" claim |

**Presentation:** Left **Continuous Noether examples** table; right **Discrete transformations and known exceptions**, with an explicit divider. Bottom line **“Symmetry is powerful but not universally exact.”** Avoid the image's existing overconfident "laws the same everywhere and everywhen" wording.

**Preferred owner decision:** replace this embedded-text-heavy figure; altering only its HTML caption would leave the false statements in an independently opened graphic.

## 4. Blueprint C — Paper 3 Figure 4.1

**Source:** `images/symmetria/paper-03/03_dirac_nilpotent_structure.webp`, SHA `e2ef7767f8f77127d67f6732ce7b58656996c0c6`.

**Actual observation:** The first panel shows a standard-looking Dirac equation; the second defines schematic `N²=0`; the third says the nilpotent formulation is "mathematically equivalent to the standard Dirac structure" without displaying Rowlands' specific algebraic construction. Bottom panels show a broad sequence toward unification/manifestations that risks confusing a studied reformulation with a new validated physical result.

**Proposed title:** **ROWLANDS' NILPOTENT APPROACH TO DIRAC STRUCTURE**.

| Panel | Exact candidate text | Display |
| --- | --- | --- |
| 1 — Established starting point | **Dirac theory:** a relativistic quantum description of spin-½ particles. | Precisely typeset `(i\gamma^\mu \partial_\mu-m)\psi=0` in natural units, label the units/conventions if displayed |
| 2 — Specified reformulation | **Rowlands' construction** uses a particular algebraic representation with nilpotent expressions under defined conditions. | Clean `N²=0` with a note **“schematic condition; operator/representation must be specified”** |
| 3 — What is and is not claimed | **An algebraic correspondence to Dirac structure is discussed for a specified construction.** This does **not** establish equivalence for every nilpotent N. | Arrow labelled **"under explicit algebraic assumptions"**, not an arrow implying generic consequence |
| 4 — Further research | **Open questions:** derivation, recovered physics, physical interpretation, and whether distinct testable consequences exist. | Research pipeline ending with **"not established by this diagram"** |

**Safe alternative if minimal editing suffices:** replace only the words "mathematically equivalent" with **"a specified algebraic reformulation of Dirac structure has been described"**, and mark cosmological/theoretical-unification panels **"Exploratory interpretation, not a demonstrated consequence."** Whether such surgery is visually acceptable depends on editable sources and actual visual evidence.

**Preferred owner decision:** controlled label replacement or targeted redraw, not an unreviewed general theory rewrite. Do not add a formal reference list to the public discussion paper.

## 5. Two additional high-severity findings from Work — reconcile now, decide later

### D — Paper 1 Figure 3.1: the Standard Model

**File:** `01_search_for_unification.webp` SHA `c6ca2f610595cd6eb2677eeae26885c80577ac0a`. Chat's actual original WebP inspection confirms the Standard Model box states **“Unifies electromagnetic, weak and strong forces.”** This is misleading: the Standard Model describes electromagnetic, weak and strong interactions; **electroweak theory** unifies electromagnetic and weak, while the strong interaction remains in a separate QCD sector.

**Minimal exact figure text:** **“Describes electromagnetic, weak and strong interactions. Electroweak theory links the electromagnetic and weak sectors.”** The graphic can retain its GUT category as a **candidate proposal**, not an accomplished grand unification. Because the incorrect statement is *embedded in the WebP*, an unrelated HTML caption does not solve standalone misinformation. Prefer precise local panel recomposition over recreating the whole infographic.

### E — Paper 4 Figure 4.1: incompatible purpose

**File:** `04_elegance_requires_empirical_test.webp` SHA `54d86da3e6878f5a219dfa7a9eb7ed98399f5871`. Full-resolution inspection confirms it is headed **“The bigger picture”** and maps speculative nilpotence ideas into quantum theory, spacetime and cosmology. Its HTML section instead explains that mathematical elegance **must face testable evidence**. The actual adjacent prose says that a square-zero algebraic expression may be striking, but its physical value depends on conditions, observables and critical testing.

**Two owner options:**
- **Minimal, retain the existing image:** recaption to describe **only proposed possible research directions** and say none has been empirically demonstrated, but accept that the image remains a weak thematic fit for the section. Consider repositioning it to a future-research discussion only if editorially appropriate.
- **Preferred educational fit:** replace Fig 4.1 with a diagram titled **“ELEGANCE IS NOT EVIDENCE”**: *Define mathematical object* → *show internal consistency* → *derive quantitative consequences* → *compare with observations* → *revise, reject or provisionally retain*. Bottom qualifier **“A beautiful equation is a starting point, not experimental confirmation.”** This directly illustrates the existing section/caption. No claim that any proposed SYMMETRIA test has actually been completed.

This is a significant subject mismatch, not a mathematical falsehood of the same kind as the P/T panel.

## 6. Paper 3 image-swap layout and adjacent-passage confirmation

The original sources have been visually inspected, and their **current adjacent article passages** checked. These are **only candidate swaps until owner approval**:

| Paper 3 position | Actual adjacent section claim | Current image | Candidate image | Result if approved |
| --- | --- | --- | --- | --- |
| Fig 1.1, Introduction | symmetry and conservation motivate more structured algebraic questions | `03_symmetry_to_nilpotence.webp` (actually Rowlands duality/anticommutativity/nilpotence) | `03_rowlands_conceptual_route.webp` (actually rotation, Noether, conservation) | Stronger image-to-introduction match |
| Fig 3.1, Peter Rowlands and foundations | duality, anticommutativity and nilpotence as specific mathematical themes | `03_rowlands_conceptual_route.webp` (actually Noether and rotational symmetry) | `03_symmetry_to_nilpotence.webp` | Stronger match to Rowlands' three mathematical themes |
| Fig 5.1, What the nilpotent might tell us | distinguish algebraic zero, zero-totality interpretation, quantum vacuum | `03_zero_totality_vacuum.webp` (actually open questions and future tests) | `03_nilpotence_to_mathematics_and_reality.webp` (actually compares three kinds of zero) | Corrects direct caption-topic mismatch |
| Fig 6.1, From Rowlands to SYMMETRIA | scientific programme and testable development remain open | `03_nilpotence_to_mathematics_and_reality.webp` (actually three kinds of zero) | `03_zero_totality_vacuum.webp` (actually future questions and experiments) | Stronger match to final transition section |

**Implementation note:** swapping only the two pairs of `src` attributes is insufficient: adjust the `alt` text to match the *actual graphic subject* after the swap, and verify the nearest paragraph plus caption. The new viewer automatically derives its accessible title from image alt; stale alt text would mislabel the zoomed standalone image. Preserve the originals and **all seven figure positions**.

**Additional caution:** The original Fig 1.1 Rowlands graphic contains **stylised, partly illegible decorative formula glyphs** in its central transparent mathematical panel. A placement swap may fix topic but does not certify that those glyphs are valid. Avoid presenting those as a derivation; propose controlled typesetting/removal if a later owner-approved figure refresh occurs. The current Noether visual has simplified action-symmetry claims which should remain qualified.

## 7. Secondary medium-severity corrections (do not blanket redraw)

- **P2 Fig 5.1**: the image depicts **general symmetry**, not the broken-symmetry mechanism in §5. If the objective is to *teach symmetry breaking*, prefer a clear ferromagnetic ordering example above/below a transition (qualify as an example, not an all-purpose physical mechanism). Otherwise recaption as "why symmetry is useful" and accept imperfect section fit.
- **P2 Figs 1.1, 2.1, 3.1**: real image topics are respectively **fragmented theories**, **vision of unification**, **patterns in nature**; their respective current captions describe different subjects. Proposal: write concise true captions, then verify that the image meaning fits the local section. If a caption makes the section incoherent, prefer targeted replacement instead of forcing a misfit.
- **P4 Fig 3.1**: the graphic is a focused Noether/symmetry example, not a comprehensive definition of elegance; recaption as one illustration of mathematical structure.
- **P4 Fig 6.1**: broad speculative applications and consciousness/technology are more extensive than the emergence caption. Qualify as future questions or replace only if the owner requires a clear emergence explanation.
- **P1 Fig 1.1**: historical development fits, but an unqualified *consciousness* endpoint does not; flag as proposed speculation.
- **P1 Fig 6.1**: multiple **undefined decorative formulae** look like derived identities; replace/qualify only if the owner elects a second correction batch.
- **P4 cover**: decorative integral symbol detached from a complete integral expression; optional cosmetic correction, not an urgent scientific claim correction.

## 8. Controlled production test checklist — for *after* owner decision

1. Inspect the actual feature SHA again before coding, pin the four HTML blob hashes and all original source WebP hashes and keep an exact rollback map.
2. Make a **finite owner-approved change-set** with exact image paths, replacement filenames, text labels, `alt` text, nearest captions, and numbered figure slots. Never silently widen the approval to all 28.
3. For an approved replacement use authored text layers, source-file versioning and visually checked WebP exports; quality setting 80 is a default encoder target, **not** a promise of 80% compression.
4. Run exact-commit `python3 -u docs/reports/scripts/v2_stage8_qa.py` and adapt its protected article integrity baseline **only for the specifically authorised main-block differences**. Do not disable broad preservation checks.
5. Run existing GitHub Actions full-suite browser QA and image viewer checks at 320/390/768/1440/1920+ widths; verify no broken image refs, no overflow, intact sticky nav, 28 figures, mobile landscape, mouse-wheel zoom, drag, pinch and accessible alt.
6. Present side-by-side original/revised figure previews, inspect formula spelling and status qualifiers both at fit-to-screen and full-size 100%/zoom, then obtain owner final visual sign-off.
7. Leave both PR #2 and PR #5 **draft/unmerged/unpublished**. No release, publication or claim that the overall SYMMETRIA physics framework is scientifically confirmed.

## 9. Approval gate proposal

Recommend the owner first select **five high-severity treatments** (P1 Figs 3.1 and 5.1; P2 Fig 4.1; P3 Fig 4.1; P4 Fig 4.1) plus **two P3 swaps**. A second, optional limited batch covers the medium mismatches and cosmetic issues. **No figure generation, edits, PR merges or deployments have been performed by this blueprint.**
