# Team Meeting Notes: 2026-11-05

Two groups worked today. Jordan, Ira, Jack and Fedor ran full robot game test runs. The rest of the team started writing the robot design speech.

## Full robot game test runs

**Who:** Jordan, Ira, Jack and Fedor. Ira kept the timing sheet ("Robot Timing, by Ira the Amazing"; scan: `full test runs.pdf`).

**Goal:** see whether all the missions work together in one run and fit inside the **2:30** match limit.

**Mission order tested** (as reported):

1. Mission 9, the tree
2. Mission 1, the drone
3. Mission 3, the seeds
4. Pushing in the skylight
5. Raising the roof at the city (the ant one)
6. The roof one

**(confirm)** the mission numbers for steps 4 to 6 and whether "the ant one" and "the roof one" are two separate missions. The notes above follow how the order was described.

### Results from the timing sheet (8 runs)

| Run | Time | Points | Touches |
|---|---|---|---|
| 1 | N/A | none written | 6 |
| 2 | N/A | none written | 2 |
| 3 | N/A | none written | 4 |
| 4 | 4:30 | none written | 3 |
| 5 | 3:42 | 150 | 8 |
| 6 | **2:50** | **185** | 3 |
| 7 | 2:52 | 145 | 4 |
| 8 | 4:34 | 140 | 9 |

How the sheet reads (**confirm** with Ira):
- "N/A" in the time column for runs 1 to 3 probably means the run did not finish, so there was no full time.
- "Touches" is probably the number of times the robot was picked up or touched during the run. In the match a touch has a cost, so fewer is better. **(confirm)**
- Points were only written for runs 5 to 8.

What it shows:
- **No run has fit inside 2:30 yet.** The best times were run 6 (2:50) and run 7 (2:52), about 20 seconds over.
- **The best run was also the cleanest:** run 6 scored the most points (185) with only 3 touches. Run 8 had the most touches (9) and the lowest points (140).
- **Run 5 and run 8 are the slow ones** (3:42 and 4:34, with 8 and 9 touches). Find out what went wrong in them.
- Runs got faster and cleaner between runs 5 and 7, but not consistently. Four runs is not enough to say the missions are reliable.

**This is test evidence for the speech.** It is repeated testing of the whole run with times, points and touches, which is what judges look for in the Iterate row.

Still needed from this group:
- Which missions were done and which failed in each run, and what caused the slow runs (5 and 8).
- What the group will change to get under 2:30 (cut a mission, speed up a move, remove touches).
- Whether the points are the real total for the missions completed.

## Robot design speech: first drafts

Everyone else filled in the speech writing sheets (scan: `robot design speech draft.pdf`, 7 pages). What was written so far, as the kids wrote it (spelling tidied):

### Section 1: Opening and mission strategy (page 3 to 4)
- **Mission strategy:** "They got us lots of points and were relatively easy. We looked at all the different missions and ranked them by two things: they needed to be able to get us lots of points, so we have a higher chance of doing better. The other way was how easy it is to achieve the mission, so we can go fast and get more missions done."
- **Why this order:** "We did the missions in that order because we wanted to get from one side to the other just once to save time."
- **Resources:** "When building and coding the robot we used bot-fluencers, conference sessions, SPIKE app and build instructions."
- **Blank:** the list of missions we attempt (the opening line does not name them), "From ___ we learned ___", and "When we got stuck we asked ___".
- The team name and a note "and our fun" were added at the top. A margin note on page 3 says "Wrong", with no clear reason. **(confirm what was wrong)**

### Section 2: Choosing and building our robot (page 4 to 5)
- **Designs and criteria:** "We looked at 4 different designs: HummerOne, Comp Bot, GummyBears / Droid Bot M and StarterBot. We scored them on six criteria all about how the robot performs in a match." The six criteria were listed: archetype match to proven competitive designs, attachment swap speed at the base, squaring (flat back and sides), stability under load, maneuverability in tight spaces, and drive repeatability (for PID code).
- **Problem noticed after building:** "After we finished building the HummerOne we noticed the front wheels would slide and create friction, which made it harder to move straight."
- **Blank:** why cost was left out, the highest score and why we chose it, and what we changed the wheels to (and why).

### Section 3: Attachments, forklift (page 6 to 7)
- **Attachment:** forklift. **Mission:** 9.
- **Where it started:** "Jack started building the forklift from Coach Zain. For the forklift, Ella and Amelia continued building it."
- **Mistakes and fix:** "We made a couple of mistakes, like when Sylvie moved up the gear bar. A problem Ella found was that certain things were built on the wrong side. Sylvie and others fixed this by going back in the instructions and rebuilding certain parts."
- **Blank:** what we changed from the original and why, and what it is good and not so good at.
- **Check:** the design log says the forklift came from `Forklift1-zoptyk.pdf`, and Coach Zain is the Comp Bot creator. Confirm which source the forklift really came from. Also the log described the forklift as raising a platform, and today it is listed for Mission 9 (the tree). Confirm which is right.

### Section 4: Code and sensors, part 1 (page 8)
- **Sensors:** "We use 2 colour sensors and 1 gyro sensor. The colour sensors sense the colours on the mat. We use them for squaring. The gyro sensor ..." (sentence not finished).
- **Why a second sensor:** "When one sensor sees the colour black, it will turn until the other sensor sees black. It will then wiggle till straight." They added that squaring is needed because the robot drives crooked without it.
- **Squaring step by step:** 1. "It drives up to the line diagonally and senses the black line." 2. "It turns until the other sensor senses the black line." 3. "It wiggles until it's straight."
- **Blank or unfinished:** what the gyro sensor does (turns and driving straight), and where each sensor is mounted.

### Not started in the scans
Section 3 for the other attachments (lifting arm and seed bucket, 2-axis with hook, Mission 1, Mission 11 basket), section 4 part 2 (Gyro Move, Kp and Ki, yaw turns, ramp, cm), section 5 (test stories), section 6, section 7, and the who-says-what table.

## What to do next

- [ ] Fill the biggest gaps in the speech: name the missions we attempt, and finish section 2 (cost, highest score, wheel change) and section 4 (gyro sensor)
- [ ] Write the test stories using real numbers: the Kp and Ki tuning, the 1 m drive, the seed basket (3, 5, 7 out of 10), and today's full test runs (best run 185 points, 2:50, 3 touches)
- [ ] Assign speakers so all 9 of us speak
- [ ] Test run group: find out why runs 5 and 8 were slow and what will get us under 2:30
- [ ] Confirm the mission numbers and order for steps 4 to 6 of the run
- [ ] Confirm where the forklift came from, and which mission it does
- [ ] Rehearse the speech out loud once it is written (target: under 5 minutes, no game field)
