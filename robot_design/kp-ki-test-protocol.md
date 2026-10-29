# Kp and Ki Test Protocol (for each attachment)

Run this test once for each finished attachment: **forklift, seed bucket, Mission 1 attachment, and 2-axis (with hook)**. Run it once more with **no attachment** as the control.

## Why test each attachment

Kp and Ki in `Gyro Move` were tuned on the bare robot (and retuned on 2026-10-13 after the Technic ball joint went on). An attachment changes the robot in ways that affect how it drives straight:

- **Weight on the front ball joint.** More weight means more drag, so the robot pulls to one side.
- **Centre of gravity.** A raised forklift or an extended 2-axis arm makes the robot top-heavy and easier to wobble.
- **Load that moves.** Seeds in the bucket, or an arm that swings, push on the robot while it drives.

The attachment might not change anything. The test tells us that, and gives us proof for the judges either way.

## What we are testing

`Gyro Move` (see [mission2/mission-2-code.md](mission2/mission-2-code.md)) corrects the heading every 0.1 s:

```text
CorrectionValue = Error * KP + KI * (Error_Sum * WaitTime)
```

- **Kp** reacts to how far off straight the robot is *right now*. Too low: it drifts. Too high: it weaves side to side.
- **Ki** reacts to how long it has been off. It fixes a steady pull to one side. Too high: the robot swings past straight and wobbles near the end. `Error_Sum` is never capped, so a big Ki builds up fast.

Current values to start from: **Kp 2.1, Ki 2** from 2026-10-06. Jordan retuned them on 2026-10-13 for the ball joint, so **confirm the numbers in the code now and write them in the baseline row of every sheet.**

## The one rule

**Change one number at a time, and repeat the exact same test.** If two things change, we cannot tell which one made the difference.

## Roles (rotate between attachments)

| Role | Job |
|---|---|
| Runner | Places the robot on the start jig and presses the button |
| Measurer | Reads the sideways offset and the distance error off the tape |
| Recorder | Writes every run on the data sheet, including bad ones |
| Coder | Changes Kp or Ki in `Gyro Move` and downloads to the hub |

## Setup (do this every time)

1. **Mat or floor:** the same flat, clean surface every time. Wipe the wheels.
2. **Tape the course:** lay a straight line of tape, 100 cm long, with a ruler or 1 m stick. Mark the end line. Measure sideways offset from the tape.
3. **Start jig:** two blocks or a wall edge so the robot starts in exactly the same place and pointing the same way every run.
4. **Reference mark:** put a small sticker on the robot's front centre. Always measure to this mark.
5. **Battery:** charged. Note the hub battery level on the sheet. Low battery changes how the motors respond, so do not compare runs at very different charge.
6. **Attachment:** fitted with **quick pins** (see design log entry 7). Check it is tight before every batch of runs.
7. **Test program:** one block, `Gyro Move` with **Distance 100 cm, Speed 90** (Mission 2 speed). Nothing else in the program.
8. **Gyro:** set the robot down and hold it still for 3 seconds after starting the program. `Gyro Move` resets yaw at the start, so do not pick the robot up or bump it until it finishes.

## What to measure on every run

| Measure | How | Units |
|---|---|---|
| **Sideways offset** | Distance from the tape to the reference mark at the end. **Right of the line = +, left = −.** | cm |
| **Distance error** | How far past (+) or short of (−) the end line the mark stopped | cm |
| **Wobble score** | Watch the run: 0 = dead straight, 1 = tiny twitch, 2 = visible weave, 3 = big swings or the attachment shakes | 0 to 3 |
| **Problem?** | Attachment shifted, robot tipped or lifted a wheel, seeds fell out, hook swung | note |

Offset tells us if the PID works. Wobble tells us if Kp or Ki is too high. A "problem" run counts as a **failed run**, whatever the offset was.

## Pass target (suggested, the team may change it)

For **10 runs in a row**, at the chosen Kp and Ki:

- Every run ends **within 2 cm** of the line, and the **average of the absolute offsets is 1 cm or less**.
- **Distance error** within 1 cm every run.
- **Wobble score 1 or lower** every run.
- **No problem runs.**
- Offsets are **not all on the same side.** If every run ends left, that is a drift, not luck.

## Procedure for each attachment

### Step 0. Pick the test conditions (worst case first)

Test the attachment in the state that is hardest on the robot, because that is how it will drive in a match. Do the whole procedure in this state, then do a **quick check** (Step 4) in the others.

| Attachment | Hardest state to test in | Quick-check states |
|---|---|---|
| **Forklift** | Raised to full height, with the payload on it | Lowered (carry position), empty |
| **Seed bucket** (lifting arm) | Loaded with the seeds in the match order | Empty, arm raised and lowered |
| **Mission 1 attachment** (confirm which build) | As carried on the way to Mission 1 | Any other arm position it uses |
| **2-axis with hook** | Both axes fully extended | Both retracted |

Also watch for **tipping when the robot stops.** `Gyro Move` slows by 8 each loop at the end, and a tall load can tilt forward. Note it as a problem if the robot rocks.

### Step 1. Baseline: 5 runs at the current Kp and Ki

Run 5 times, record all five, and calculate the average of the absolute offsets.

- **If all 5 meet the pass target, stop here for this attachment.** The attachment does not need new numbers. Go to Step 3 to confirm with 10 runs, or stop and move on if short on time.
- **If not, go to Step 2.** Use the table below to guess what is wrong, then tune.

| What you see | Likely cause | First thing to change |
|---|---|---|
| Ends the same side every run, no weave | Steady pull (the weight is lopsided, or friction) | Ki up. Also check the attachment is centred on the bar. |
| Weaves left and right the whole way | Kp too high | Kp down |
| Slowly curves away and Ki does not help | Kp too low | Kp up |
| Straight for most of the run, then swings or wiggles at the end | Ki too high (builds up) | Ki down |
| Works with the attachment raised but not lowered (or the reverse) | Weight position changes the pull | Test both, then choose one set that works for both |

### Step 2. Tune: Kp first, then Ki

**Tune Kp first with Ki set to 0.** Ki hides what Kp is doing, so turn it off while choosing Kp.

#### 2a. Kp sweep (Ki = 0), 3 runs each

Try each value, keeping everything else the same. Test the starting value from the baseline plus the ones either side.

| Kp to try | Runs | What we want to see |
|---|---|---|
| 1.0 | 3 | Probably drifts |
| 1.5 | 3 | |
| 2.0 | 3 | |
| 2.5 | 3 | |
| 3.0 | 3 | Probably starts to weave |

**Choose the Kp with the smallest average offset where the wobble score is 1 or lower.** If two are close, take the lower one, because a lower Kp is gentler on the attachment.

If the best value is at the edge of the table (1.0 or 3.0), extend the sweep one more step in that direction.

#### 2b. Ki sweep (with the chosen Kp), 3 runs each

| Ki to try | Runs | What we want to see |
|---|---|---|
| 0 | 3 | Already measured in 2a, copy the result |
| 0.5 | 3 | |
| 1 | 3 | |
| 2 | 3 | Current value from 2026-10-06 |
| 3 | 3 | Watch for swinging at the end |

**Choose the smallest Ki that stops the one-sided drift.** If Ki 0 already passes, use Ki 0. A smaller Ki is safer because the error total is never capped.

Ki matters most on long drives, so if the chosen Ki is small, also run a 150 cm drive as a check.

### Step 3. Confirm: 10 runs at the chosen Kp and Ki

Run 10 times in a row with the chosen numbers and no changes. Record every run. If the 10 runs meet the pass target, the numbers are **confirmed** for this attachment. If one run fails, do not throw it out. Note why, and decide whether to retune or whether it was a setup mistake (robot bumped, gyro not still).

This 10-run result is the evidence for the design log (see "Where to keep results").

### Step 4. Quick check in the other attachment states

Use the final Kp and Ki and run **3 times** in each of the quick-check states from Step 0. Each should still meet the pass target. If one state fails, the numbers are a compromise. Retest at the other settings, or choose the setting that works in the state used while driving the farthest.

### Step 5. Short drive check

Missions often move only 7 to 30 cm (Mission 2 uses about 6.8 cm and 30.2 cm). Ki needs time to build up, so a short drive tests mostly Kp. Run **3 times at 30 cm** and write down the result. A 30 cm drive should end within 1 cm of the line and show no wobble.

## Control run: no attachment

Do the full procedure once with **no attachment** so we have a reference. It also catches problems that have nothing to do with the attachments, like a dirty wheel or the ball joint. Every attachment is compared against this row.

## If the attachments need different numbers

The `Gyro Move` block has `KP = 2.1` and `KI = 2` written into it. Two options:

1. **One shared set** that passes the pass target on all four attachments. This is simpler, so try it first. If the best Kp and Ki per attachment are within about 0.5 of each other, use the one that gave the best average across them.
2. **Kp and Ki as inputs to the block.** If the attachments really need different numbers (for example the forklift needs a much lower Kp), add Kp and Ki as inputs to `Gyro Move`, and pass the right pair from each mission program. Keep a copy of the working block before changing it.

Record which option we used in the design log.

## Data sheet (copy one per attachment)

**Attachment:** ________________  **Test state:** ________________  **Date:** ________  **Battery:** ______%
**Team:** Runner ________  Measurer ________  Recorder ________  Coder ________

| # | Test | Kp | Ki | Offset (cm, right +) | Distance error (cm) | Wobble (0 to 3) | Problem? |
|---|---|---|---|---|---|---|---|
| 1 | Baseline | | | | | | |
| 2 | Baseline | | | | | | |
| 3 | Baseline | | | | | | |
| 4 | Baseline | | | | | | |
| 5 | Baseline | | | | | | |
| 6 | Kp sweep | | 0 | | | | |
| 7 | Kp sweep | | 0 | | | | |
| 8 | Kp sweep | | 0 | | | | |
| 9 | Kp sweep | | 0 | | | | |
| 10 | Kp sweep | | 0 | | | | |
| 11 | Kp sweep | | 0 | | | | |
| 12 | Kp sweep | | 0 | | | | |
| 13 | Kp sweep | | 0 | | | | |
| 14 | Kp sweep | | 0 | | | | |
| 15 | Kp sweep | | 0 | | | | |
| 16 | Kp sweep | | 0 | | | | |
| 17 | Kp sweep | | 0 | | | | |
| 18 | Kp sweep | | 0 | | | | |
| 19 | Kp sweep | | 0 | | | | |
| 20 | Kp sweep | | 0 | | | | |
| 21 | Ki sweep | | | | | | |
| 22 | Ki sweep | | | | | | |
| 23 | Ki sweep | | | | | | |
| 24 | Ki sweep | | | | | | |
| 25 | Ki sweep | | | | | | |
| 26 | Ki sweep | | | | | | |
| 27 | Ki sweep | | | | | | |
| 28 | Ki sweep | | | | | | |
| 29 | Ki sweep | | | | | | |
| 30 | Ki sweep | | | | | | |
| 31 | Ki sweep | | | | | | |
| 32 | Ki sweep | | | | | | |

Add rows as needed. For the Step 3 confirm runs use a fresh table of 10 rows, with the final Kp and Ki written in the header.

**Step 3 confirm (10 runs):** final **Kp ______  Ki ______**

| Run | Offset (cm) | Distance error (cm) | Wobble | Problem? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
| **Average of absolute offsets** | | | | |
| **Worst run** | | | | |
| **Pass?** | | | | |

## Summary table (fill in at the end)

One row per attachment, so the team and the judges can see the whole picture.

| Attachment | State tested | Baseline Kp / Ki | Baseline average offset | Final Kp | Final Ki | Final average offset (10 runs) | Wobble (worst) | Problems | Pass? |
|---|---|---|---|---|---|---|---|---|---|
| No attachment (control) | | | | | | | | | |
| Forklift | | | | | | | | | |
| Seed bucket | | | | | | | | | |
| Mission 1 attachment | | | | | | | | | |
| 2-axis with hook | | | | | | | | | |

## Time needed

| Case | Runs | About |
|---|---|---|
| Baseline passes, then 10 confirm runs | 15 | 15 minutes |
| Full tune (Kp sweep, Ki sweep, confirm, quick checks, short drive) | about 50 | 45 to 60 minutes |

Four attachments plus the control is **two meetings** if two groups run in parallel, each with its own robot, or about three if one robot does them all. Test the control first so the groups share one result.

## Where to keep results

1. Photograph or scan each data sheet and keep it with the design log material.
2. Add the final Kp and Ki for each attachment to the table in [mission2/kp-ki-tuning.md](mission2/kp-ki-tuning.md).
3. Add a short entry to [design-log.md](design-log.md) per attachment: what the attachment did to the robot, what changed (or "nothing changed, and here are 10 runs that prove it"), and the average offset.

Judges like to see repeated testing, a change that was made for a reason, and a result. A "no change needed" result with 10 recorded runs is as good as a retune.
