# Completed Worksheets, 2026-10-29 (transcription)

A transcription of the sheets the team filled in at the 2026-10-29 meeting: the Robot Design Log worksheet (mostly handwritten answers) and some of the Kp/Ki test sheets. The scans are `look it's a giraffe robot design.pdf` and `robot design additional pages.pdf`, plus four photos of the attachments. This page is a record of what was written. It has **not** been merged into [design-log.md](design-log.md) or [mission2/kp-ki-tuning.md](mission2/kp-ki-tuning.md) yet.

Handwriting is copied as written (spelling kept). **[?]** marks a word or number that is hard to read. **Check** marks something that needs a person to confirm.

## What was and was not returned

| Sheet | Returned? |
|---|---|
| Design log worksheet pages 1 to 8 (entries 1 to 11, final pick) | Yes. Entries 8, 10 and the final pick are blank. |
| Design log worksheet page 9 (forklift), 11 (Mission 1), 14 to 15 (anything we forgot) | **Not in the scans** |
| Design log worksheet page 10 (seed bucket), 12 (2-axis) | Yes (second PDF) |
| Design log worksheet page 13 (test results) | Yes, the 1 m drive only |
| Kp/Ki: control (no attachment), sheet 1 | Yes, mostly complete |
| Kp/Ki: forklift sheet 1, 2-axis sheet 1 | Started, 2 runs each |
| Kp/Ki: seed bucket, Mission 1, all of sheet 2, summary | **Not in the scans** |
| Photos | 4 photos, and 2 notebook sketches of the original builds (2-axis and lifting arm) |

## Kp/Ki results (the part that matters for the code)

### Control (bare robot), 2026-10-29

Runner and measurer: Jackathon. Recorder: Fedor. Coder: Jordan. Battery 100%. The sheet asked for cm, but **every measurement is written in mm** (see "Check" at the end).

**Step 1. Baseline at the old values (Kp 2.1, Ki 2), 5 runs**

| Run | Offset side | Miss (written) | Wobble |
|---|---|---|---|
| 1 | + (right) | 12.6 mm | 1 |
| 2 | + | 7.4 mm | 1 |
| 3 | + | 14 mm | 1.5 |
| 4 | − (left) | 5.5 mm | 1 |
| 5 | − | 8.6 mm | 1 |

Average written as "9.0 mm" **[?]**. The five numbers average 9.6 mm. The team ticked "All 5 pass: Yes."

**Step 2a. Kp sweep with Ki = 0** (offset in mm, + is right; wobble 0 to 3)

| Kp | Run 1 | Run 2 | Run 3 | Average miss (written) |
|---|---|---|---|---|
| 1.0 | +23.9 (1.5) | +26.1 (1.5) | +29.4 (1.5) | 26 |
| 1.5 | +19 (1.5) | +23 (1.5) | +2.8 (1.5) | 15 |
| 2.0 | +1.8 (1) | 0 (1) | 0 (1) | 0.6 |
| 2.5 | +10.6 (1) | +5.4 (1) | 15.7 (1.5) | "2" **[?]** (the numbers average 10.6) |
| 3.0 | +10.7 (1.5) | +5.9 (0.5) | 23.3 (3) | 13 |
| 2.1 (spare row) | 0 (1) | 10.2 **[?]** (1.5) | not recorded | |

**Chosen Kp: 2.** No reason written.

**Step 2b. Ki sweep with Kp = 2**

| Ki | Run 1 | Run 2 | Run 3 | Average miss (written) |
|---|---|---|---|---|
| 0 | +6.6 (1.2) | not recorded | not recorded | |
| 0.5 | +12.8 (1) | +6.6 (1.2) | +20.4 (1) | |
| 1 | 0 (1) | +1.6 (1) | 0 (1) | "<1 mm" |
| 2 | 0 (1) | +17.5 (1) | −2 (1) | "6 mm" |
| 3 | not run | | | |

**Chosen Ki: 1.** Reason written: "Error was lowest".

**What it shows**
- **Kp 2 with Ki 1 is the best pair tested.** The three runs ended within 1.6 mm of straight, and the old Kp 2.1 / Ki 2 baseline averaged about 9.6 mm.
- **Low Kp drifts right, high Kp weaves.** Kp 1.0 and 1.5 ended far to the right (19 to 29 mm) with wobble 1.5. Kp 3.0 had a wobble score of 3 on one run. This is what the protocol predicts.
- **The data is noisy.** The Ki 0.5 and Ki 2 rows have runs of 17 to 20 mm next to runs near 0, so 3 runs per value is not enough to rank them. The 10-run confirm (sheet 2) at Kp 2 / Ki 1 is still to do.
- **Nearly every miss is to the right.** Only Baseline runs 4 and 5 and one Ki 2 run went left. That points to a steady pull right on the bare robot. Check for a wheel or ball joint problem.

### Forklift and 2-axis (baseline only, started)

Both sheets list **Current Kp 2, Current Ki 1**, which are the new values from the control tuning. No date, battery or names were filled in. The two sheets have only 2 runs each.

| Attachment | Run | Offset side | Miss (written) | Wobble | Other |
|---|---|---|---|---|---|
| Forklift | 1 | + | 3.5 mm | 1 | "−12 mm over 100 cm" **[?]** in the Problem column |
| Forklift | 2 | − **[?]** | not written | 1 | "−13.2 mm" in the Problem column |
| 2-axis | 1 | + | 3.6 mm | 1 | |
| 2-axis | 2 | + | 8.8 | 1 | |

The forklift's "−12 mm over 100 cm" and "−13.2 mm" may be **distance** error (the robot stopping short), not sideways error. Check.

### Design log page 13: drive 1 m (100 cm), ten times

The Kp and Ki used are not written. The "Off by" column was filled in; the "Ended at" column was not.

| Run | Off by (written) |
|---|---|
| 1 | 7.2 mm |
| 2 | 2.9 mm |
| 3 | −4.0 mm |
| 4 | −3.6 mm |
| 5 | 9.1 mm |
| 6 | "Perfect" |
| 7 | "less than 2" |
| 8 | "less than 2" |
| 9 | "less than 2" |
| 10 | "Perfect" |

The 10 turns of 90 degrees and the ruler squaring check were left blank.

## Design log worksheet answers

### 1. HummerOne as base robot (page 3)
- **Why HummerOne?** "Hummer had the most good qualities like, its stability."
- **What do you remember about building it?** "I remembers modifying the robot's mini wheels because we didn't have the right ones."
- **Ruler squaring check:** blank.

### 2. Scoring the four designs (page 3)
- **Which criterion mattered most?** "Drive repeatability matters the most to me. It is important to me and Ella because we need consistency."
- **A score you disagreed with?** "Not really."
- **Why was cost left out?** "Because we didn't care about the cost."

### 3. Mine cart wheels (page 4)
- **Who changed the wheels?** Sylvie. **Date:** "September" (written over a crossed-out entry).
- **Why mine cart wheels and not another?** "Cuz they fit, and the better option was too tall."
- **How did you notice they stuck out?** "She looked. (direct quote)". Sylvie's name is written above both "you" in the question.

### 4. Second colour sensor (page 4)
- **Where is it mounted, and why?** "There are 2 colour senses. They are there to sense colour." (This does not say where. **Check.**)
- **Before and after squaring:** "Without the squaring it drove crooked and with the squaring it didn't."
- **Which mission models have a line to square on?** blank (a drawing instead).

### 5. Mini ball caster (page 5)
- **Why "mini"?** "Cuz it could do more stuff and could get closer to certain missions."
- **Did it drift?** "Yes, it is being fixed."
- Header corrected to credit **Ira** (the original credited Fedor and Ira; a name is crossed out).

### 6. Attachments on the mounting bar (page 5)

| Attachment | Pros | Cons | Rating (1 to 5) |
|---|---|---|---|
| Lifting arm + seed bucket | "Masher good" **[?]** | "Not high enough" | 3.5 |
| 2-axis + hook | "It works" | "gears fall off" | 5 |
| Forklift | "Its cool" | "Swinging it gets stuck" **[?]** | 3.5 |

- **Did the forklift tip when raised?** "Yes, and we stabilized it so it's good now!"
- **Who built each, and what changed?** "We all collaborated on attachments."

### 7. Quick pins (page 6)
- **What did Jack hope axle pins would do?** "It would be faster to put on off."
- **When Jack suggested it, and whether the 2-axis and forklift also came off:** blank.

### 8, 10. Gyro blocks, distances in cm (pages 6 and 7)
Blank. The Mission 2 test results and the Move 1 and Move 2 distances in cm still need answers from Jordan or Fedor.

### 9. Technic ball joint (page 7)
- **Which part?** "Technic ball joint" (with a small drawing of it).
- **Describe the wobble:** "When the robot is unstable the robot starts wiggling and wobbling."
- **Does it drift when accelerating or reversing?** blank. (Entry 5 says the caster drift "is being fixed.")

### 11. Mission 11 seed basket (page 8)

| Idea tried | Catches out of 10 | What happened |
|---|---|---|
| Walls on the side | 3 | "it fell out a lot" |
| Change the code | 5 | "didn't go high enough" |
| Bowl / basket | 7 | "it also fell out a lot" |

**Context (confirmed):** removing the seed on Mission 11 is worth **30 points**, but the team wants to **collect the seed** to use in another mission later. The bowl/basket (7 out of 10) is the best of the three. The seed still falls out sometimes.
Relation to the seed bucket, and the final attachment pick: blank.

### 13. Seed bucket on the lifting arm (page 10)
- **Change 1, arm end:** original "plain geared hinge arm", now "added a seed bucket". Why: "We wanted to make it so we could bring the seed back and the plain geared hinge arm didn't work well."
- **Change 2, pins:** original axle pins, now quick pins. Why: holds more securely. (This text was pre-printed from the log.)
- Seed order, and how the seeds come out: blank. Change 3: blank.

### 15. 2-axis movement with hook (page 12)
- **Change 1, end of arm:** original no hook, now a hook. Why: "It is more convenient for pulling down the door." (The first three lines of this change were pre-printed from the log.)
- **Change 2, swapped sides:** original "different sides", now "opposite sides". Why: "so that it works better".
- **Change 3, extended wacker stick:** original "short wacker stick", now "a long pole with minimal" **[?]**. Why: "so it would reach the seed".
- **Which mission does the hook do?** "The hook does Mission 11 and hooks on to the door."
- **Gear slip or backlash:** blank. The photo drawing boxes are empty (see sketches below).

## Photos and sketches

| File | What it shows (from the image) |
|---|---|
| `20261029_172439.jpg` | The **passive Mission 1 attachment** (top view, frames and a long brown beam on the left) |
| `20261029_172506.jpg` | The **2-axis arm** (side view, arm built from yellow and black beams) |
| `20261029_172541.jpg` | The **forklift**: a tall black mast on the robot with forks at the front and a gear on top |
| `20261029_172628.jpg` | The **seed bucket**: a magenta tray on a yellow arm, with a long black rod |
| `robot design additional pages.pdf` pages 3 and 4 | Notebook sketches labelled "2 Axis Movement OG" and "Lifting arm OG" (the original builds) |

The two sketches can go in the "Original build" boxes for entries 13 and 15.

## Things to check with the team

1. ~~Units.~~ **Confirmed: the measurements are mm** (the sheets asked for cm). 9.6 mm is 0.96 cm, which just passes the 1 cm average target.
2. **Which Kp and Ki are in the code?** The control sheet chose **Kp 2, Ki 1**, replacing 2.1 / 2. **Confirmed: the code still needs the final update of Kp and Ki for each attachment.** Which values the 1 m drive test used is still not known.
3. **Missing sheets are incomplete, not lost.** The seed bucket and Mission 1 Kp/Ki sheets, every sheet 2 (the 10 confirm runs), the forklift and Mission 1 design log pages, and the summary have not been finished yet.
4. ~~Which attachment is in photos 1 and 2.~~ **Confirmed: photo 2 is the 2-axis arm and photo 1 is the passive Mission 1 attachment.**
5. **Blank answers that judges are likely to ask about:** Mission 2 test results, the distances in cm, how Kp and Ki were tuned, ruler squaring, turn accuracy, and the final attachment pick.
