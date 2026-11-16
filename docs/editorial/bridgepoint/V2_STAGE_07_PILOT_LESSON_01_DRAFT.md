# BridgePoint — Lesson 01: The Language of Mathematics

**Category:** 1 — The Mathematical Toolkit  
**Lesson:** 01 of 16  
**Status:** **Draft for editorial and mathematical review — not published**  
**Audience:** interested beginners; no advanced mathematical background assumed  
**Learning outcome:** Interpret variables, functions, powers, equations and scientific notation  
**Source for title/outcome:** [SymTech programme series catalogue](../../PROGRAMME_SERIES_STRUCTURE.md)

> **Why this matters:** Physics uses mathematics to describe patterns precisely. A letter, a unit or an equation can carry a great deal of information once you know how to read it. The aim here is to learn that language, not to memorise every symbol.

## What you will learn

By the end, you should be able to:

1. Explain what a **variable** stands for and why units matter.
2. Read a simple **equation** and rearrange it to find an unknown quantity.
3. Understand what a **function** such as \`d(t)\` means.
4. Interpret **powers** and **scientific notation**.
5. Check a calculation for sensible units and assumptions.

## 1. Letters can stand for measurable quantities

Suppose we want to describe how far something travels.

Instead of repeating a long sentence, we can use symbols:

\[
d=vt
\]

In this equation:

- \(d\) is the **distance travelled**;
- \(v\) is **speed**;
- \(t\) is **time**;
- the letters next to each other in \(vt\) mean **multiply**: \(v\times t\).

Each letter is a *variable*: a symbol representing a quantity whose value can change between situations.

**A crucial qualification:** \(d=vt\) describes distance travelled when speed stays constant throughout the interval. It does not describe every journey or automatically give the straight-line separation between the start and end points.

### Units are part of the meaning

If speed is in **kilometres per second** (\(\mathrm{km/s}\)) and time is in **seconds** (\(\mathrm{s}\)), then:

\[
\frac{\mathrm{km}}{\mathrm{s}}\times\mathrm{s}=\mathrm{km}
\]

The seconds cancel, leaving kilometres — exactly the unit we expect for distance.

This is called a **dimensional check**. It does not prove that the model is physically appropriate, but it can expose mistakes in a calculation.

## 2. How to read and rearrange an equation

An equals sign tells us that the quantities on each side have the same value.

To find speed from distance and elapsed time, start with:

\[
d=vt
\]

Divide *both* sides by \(t\), provided \(t\neq0\):

\[
\frac{d}{t}=\frac{vt}{t}=v
\]

So:

\[
v=\frac{d}{t}
\]

Nothing mysterious happened: we performed the same valid operation on each side, preserving the equality.

### Worked example — a hypothetical moving probe

Imagine a probe moving along its path at a **constant speed of 7 kilometres per second** for **10 minutes**. These values are hypothetical, not measurements from a named mission.

**Step 1 — Put the time in seconds.**

\[
10\ \mathrm{minutes}=10\times60=600\ \mathrm{s}
\]

**Step 2 — Substitute into the equation.**

\[
d=vt=7\ \mathrm{km/s}\times600\ \mathrm{s}
\]

**Step 3 — Calculate and check the units.**

\[
d=4200\ \mathrm{km}
\]

**Interpretation:** the probe travels **4,200 kilometres along its path** during those ten minutes. If its path curves, that distance is not the same thing as its straight-line displacement.

**Quick check:** If the probe travelled 4,200 km in 600 s, then \(v=4200/600=7\ \mathrm{km/s}\), matching our starting value.

## 3. Functions describe how one quantity depends on another

An expression such as

\[
d(t)=7t
\]

is read **“distance as a function of time”**. Here \(t\) is measured in seconds and the result \(d(t)\) is in kilometres; the coefficient 7 therefore represents \(7\ \mathrm{km/s}\).

The parentheses do **not** mean multiplication. \(d(120)\) means *the distance value when time is 120 seconds*.

For this simple constant-speed model:

| Time \(t\) (seconds) | Distance \(d(t)\) (kilometres) |
| ---: | ---: |
| 0 | 0 |
| 60 | 420 |
| 120 | 840 |
| 180 | 1260 |

A **function** is a rule that assigns an output to each allowed input. Here the input is elapsed time, and the output is distance travelled from the starting point. For this example we use \(t\ge0\).

More complicated physics uses functions to describe quantities that change at different rates — for example, position during an orbit or temperature during re-entry.

## 4. Powers and very large or small numbers

A *power* tells you how many times a number is multiplied by itself:

\[
10^2=10\times10=100
\]

\[
10^3=10\times10\times10=1000
\]

A negative power expresses division by a positive power:

\[
10^{-3}=\frac{1}{1000}=0.001
\]

Scientists use these powers to write large or small quantities more compactly. This is called **scientific notation**:

\[
4200\ \mathrm{km}=4.2\times10^3\ \mathrm{km}
\]

\[
0.006\ \mathrm{s}=6\times10^{-3}\ \mathrm{s}
\]

In standard scientific notation, the number before the power of ten is at least 1 but less than 10 in magnitude (except when the whole value is zero).

Computer programs often display \(4.2\times10^3\) as \`4.2e3\`. This means the **same number**, not a new unit.

### Why this helps with space research

Distances in astronomy can be extremely large, while some physical effects and measurement errors can be very small. Scientific notation makes the sizes easier to compare while keeping the units visible. It does not, by itself, tell us how accurately a quantity was measured.

## 5. Always ask what an equation assumes

A correct calculation can still answer the wrong question.

The relation \(d=vt\) is useful for **constant speed**. If speed changes, the simple multiplication no longer gives the distance without additional information.

Similarly, a mathematical expression can be well formed and still fail as a model of nature. To evaluate a physical claim, we must eventually ask about its definitions, assumptions, comparison with established evidence and possible tests.

This distinction matters in SymTech Ventures:

- **BridgePoint** teaches the mathematics.
- **SYMMETRIA** explores theoretical questions.
- **NSRP** asks whether proposed mathematical structures withstand scrutiny.
- **SEIP** considers bounded computational and engineering investigations.

Learning an equation does not establish that a speculative physical theory is true.

## Common misunderstandings

| Misunderstanding | Better interpretation |
| --- | --- |
| “A letter always represents the same number.” | A variable's value depends on the problem and its definition. |
| “The equals sign means ‘calculate the answer’.” | It states that the expressions on both sides are equal. |
| “\(d(t)\) means \(d\times t\).” | In function notation, \(d(t)\) means the output at input \(t\). |
| “\(10^3\) is 10 multiplied by 3.” | It is \(10\times10\times10=1000\). |
| “If the units work, the theory must be correct.” | Consistent units are necessary for many physical equations, but not sufficient evidence. |

## Test your understanding

Try these before looking at the solutions.

1. A hypothetical object travels at a constant **5 km/s** for **180 seconds**. How far does it travel along its path?
2. Express **48,000 km** in scientific notation.
3. A model gives \(d(t)=3t\), with \(t\) in seconds and \(d\) in kilometres. What is \(d(40)\), and what constant speed does the model represent?
4. Convert \(2.5\times10^3\ \mathrm{m}\) into kilometres.

<details>
<summary>Show answers and explanations</summary>

1. \(d=vt=5\ \mathrm{km/s}\times180\ \mathrm{s}=\mathbf{900\ \mathrm{km}}\).
2. \(\mathbf{4.8\times10^4\ \mathrm{km}}\), because \(10^4=10{,}000\).
3. \(d(40)=3\times40=\mathbf{120\ \mathrm{km}}\). The speed is \(\mathbf{3\ \mathrm{km/s}}\).
4. \(2.5\times10^3\ \mathrm{m}=2500\ \mathrm{m}=\mathbf{2.5\ \mathrm{km}}\).

</details>

## Recap

A **variable** stands for a quantity. An **equation** states a relationship. A **function** gives an output for an input. **Powers** and **scientific notation** make numerical scales manageable. Checking units and assumptions is just as important as doing the arithmetic.

These are the first tools we need before tackling vectors, motion, waves and the mathematical structures of modern physics.

## Going deeper — optional

- Try creating your own distance function for a constant speed of \(2.5\ \mathrm{km/s}\). What distance does it give after four minutes? Remember to convert the time to seconds.
- Ask whether *distance travelled* and *displacement* can differ. Draw a path that curves back towards its starting point.
- In the next lesson, **Vectors, Geometry and Space**, we will use direction as well as size to describe motion.

---

**Editorial status:** This is an **unpublished draft** prepared for Stage 7 checking. No claim of independent peer review, measured spacecraft performance or validation of SYMMETRIA is made. Its mathematical examples and interpretation must be reviewed before a real lesson link appears on the site.
