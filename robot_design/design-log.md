# Robot Design Decision Log

A running record of each robot design decision: what we chose, what we considered, and why. Judges ask *why this base* and *what did you change*, so each entry is written to answer that. Newest entries go at the bottom of the log.

**Entry template**

- **Decision:** what we chose
- **Date / who:** when and which team members
- **Options considered:** what else was on the table
- **Why:** the reasoning and the evidence behind it
- **Result / follow-up:** what happened, or what we still need to check

Items marked **(confirm)** are still guesses or missing details. Have the team member who did the work correct them.

## Summary

| # | Date | Decision | Why, in one line |
|---|---|---|---|
| 1 | 2026-09-17 to 09-22 | Chose HummerOne as the base robot to build first (shortlisted four designs) | Free, a full-width attachment bar, and a perimeter frame that should square well |
| 2 | 2026-09-22 | Scored four designs on match performance; HummerOne ranked first, 23/30 | Highest on archetype match, attachment swap and stability, with no weak spot |
| 3 | After the build, before 2026-10-01 | Replaced the front wheels with mine cart wheels | Lower profile and less friction when turning than the original rubber-less wheels, but still not flush with the sides |
| 4 | 2026-09-27 to 09-29 | Jack added a second colour sensor | Gym testing showed squaring on a line is impossible with one sensor |
| 5 | Postponed from 2026-10-01 | Switch the front support to a mini ball caster | Almost no friction, turns best, small, and it sits below the body so nothing sticks out the sides |
| 6 | 2026-10-01 | Adapted two attachments to the HummerOne mounting bar | Lifting arm gained a seed bucket, and 2-axis gained a hook |
| 7 | 2026-10-01 | Tried axle pins for attachments, went back to quick pins | The lifting arm kept coming off with axle pins; quick pins hold more securely |
| 8 | 2026-10-06 | Gyro-based PID driving and turning My Blocks (Jordan), used in Mission 2 code (Jordan, Fedor) | Gyro heading correction keeps the robot straight and turns accurate, so runs repeat |

---

## 1. Selection of the starter robot: HummerOne

- **Date / who:** Research and shortlist 2026-09-17; decision 2026-09-22. Starter bot group: Sylvie, Brynn, Jack on 09-17. Fedor, Ira and Jordan joined the build after the 09-22 regroup.
- **Options considered:**

  | Design | Source | Cost | Notes |
  |---|---|---|---|
  | HummerOne | Next Level Teacher | Free with FLL FastTrack course signup | 73 build steps, full-width attachment bar, video build support |
  | Comp Bot | Zain Khan ("Coach Zain") | Free | 225 steps (158 of them frame), enclosed frame, two attachment motors |
  | StarterBot | Robotics Rules | $30 | Compact, one SPIKE Prime set, gear-coupled attachments |
  | GummyBears / Droid Bot M | GummyBears Robotics and the Seshan Brothers | Free | Light and quick to build, weakest squaring |

  We also looked at free alternatives to StarterBot (the Pybricks 26-step SPIKE StarterBot and the FLL Tutorials base robot video). Team TurtleBots and Giraffes #3388 had no usable build instructions.
- **Why:**
  - **We built to the performance criteria, not the price.** It topped our own scoring (see entry 2).
  - **Attachments swap fast.** The full-width attachment bar lets attachments glide on and off. Our review put it at about a 5 second swap versus 20 seconds for a pinned design. That matters because we are building several Mission 1 attachments.
  - **It should square well.** Its perimeter frame gives flat side and rear panels. The review flagged one thing to check: the front-left drive wheel might sit proud of the frame.
  - **It is reasonable to build and free.** At 73 steps it takes a meeting or two, about a third of Comp Bot's length, with video and coding lessons so a stuck subteam can unblock itself.
  - **We decided not to buy StarterBot.** The $30 price bought nothing the free options didn't cover, and its sides are not flat, which is weak for squaring.
- **Result / follow-up:** The HummerOne build is **complete** as of 2026-10-01 (drivetrain finished 09-22). The squaring check with a ruler (body should touch before any wheel; watch the front-left drive wheel) will be done after the mini ball caster goes on (see entry 5), since the caster sits below the body instead of on the sides.

## 2. Scoring the four designs

- **Date / who:** 2026-09-22, whole team, in the scoring workbook (`team/resources/2026-09-22/robot-design-scoring.xlsx`). The pre-meeting review of 2026-09-21 (`Claude outputs/robot-design-review.md`) supplied reference scores and background.
- **Method:** Six criteria, each 1 to 5, equal weight, 30 points maximum. All six are about how the robot performs in a 2.5 minute match. Cost, build time and parts count were deliberately left out and treated as a separate decision afterwards. The review's reference scores came from 3D renders and published claims, not built robots.
- **Our scores:**

  | Criterion | HummerOne | Comp Bot | GummyBears / Droid Bot M | StarterBot |
  |---|---|---|---|---|
  | Archetype match to proven competitive designs | 4.5 | 2 | 4 | 2.5 |
  | Attachment swap speed at base | 4 | 3 | 3 | 2 |
  | Squaring (flat back and sides) | 4 | 5 | 3 | 2 |
  | Stability under load | 4 | 4.5 | 3 | 2 |
  | Maneuverability in tight areas | 3 | 2 | 4 | 4 |
  | Drive repeatability (for PID code) | 3.5 | 4 | 3 | 2 |
  | **Total (of 30)** | **23** | **20.5** | **20** | **14.5** |
  | **Rank** | **1** | 2 | 3 | 4 |

- **Why it came out this way:**
  - HummerOne has no weak spot, and its worst score is 3. Comp Bot beats it on squaring and repeatability, but we scored it much lower on archetype match and attachment swap.
  - GummyBears and Droid Bot M were scored as one design because the two published builds produce near-identical robots.
  - Our scores differed from the pre-meeting review, which had Comp Bot first at 26 and HummerOne tied with StarterBot at 24. Where we disagreed, the team's own view carried.
  - Squaring was scored from renders. The review said the definitive test is a ruler against each face of the built robot.
- **Result / follow-up:** HummerOne chosen. Write-up of the reasoning started here. 

## 3. Front wheels: HummerOne's originals replaced with mine cart wheels

- **Date / who:** After the HummerOne build was complete, before 2026-10-01. **(confirm who and the date)**
- **What changed:** HummerOne's front/trailing wheels have no rubber. We replaced them with mine cart wheels.
- **Options considered:** Keep the original wheels; mine cart wheels; a ball caster (see entry 5).
- **Why:**
  - Wheels without rubber make a poor support point. They skid or drag differently from run to run, which hurts the repeatability we need for PID driving and gyro turns.
  - The conference session "How to Build a Functional Robot" (09-27, presented to us by Ira and Fedor) gave the guidance we followed: **smaller wheels wobble less and are more accurate, and accuracy matters more than speed.**
  - **Why mine cart wheels in particular:** they are lower profile and create less friction when turning than the originals.
  - **What didn't work:** they still were not flush with the sides of the robot, so a wheel can touch a wall before the body does. That hurts squaring against a wall, which is one of the things we scored HummerOne on.
- **Result / follow-up:** Better than the originals but not good enough for squaring. We are replacing them with a ball caster (entry 5).

## 4. Second colour sensor

- **Date / who:** Between 2026-09-27 and 2026-09-29, after the Bayview Glen conference. **Jack added it.** Listed as done in the 09-29 notes.
- **Options considered:** Stay with one colour sensor, or add a second.
- **Why:**
  - At the conference, the Programming 201 session (Jack and Jordan attended) showed that **squaring up on a line needs two colour sensors.** When one sensor sees black, the robot turns until the other also sees black, then wiggles until it is straight on the line.
  - We tested in the gym and **could not square up with only one sensor.**
  - It matters because setup mistakes at the table (the robot placed slightly crooked) stop costing us points once the robot straightens itself on a line. The team also noted that several mission models have lines in front of them.
  - The Functional Robot session also said to shield colour sensors from room light. We judged our shielding fine for now, since we use few sensors and they worked unshielded. Revisit if readings change at an event.
- **Result / follow-up:** **The square-up program is done** (2026-10-01). Still to do: find which lines in front of mission models we can square up on, and show a judge the before/after of squaring.

## 5. Mini ball caster instead of wheels at the front (postponed)

- **Date / who:** Recommended by Fedor and Ira on 09-29. Planned for the 2026-10-01 meeting, **postponed because Ira and Fedor, who recommended it, were out sick.** Next meeting.
- **Options considered:** Original rubber-less wheels, mine cart wheels (entry 3), ball caster.
- **Why:**
  - A ball caster has **almost no friction, turns best, and is small.** That is the recommendation Fedor and Ira brought back from the conference.
  - Less friction at the front should mean the drive wheels alone set how the robot turns and drives, which suits gyro turns and the PID straight drive.
  - **It sits below the body instead of on the sides.** The mine cart wheels stuck out past the sides and spoiled squaring. A caster underneath leaves the sides clear, so the flat body faces can touch a wall first.
  - We chose the **mini** size because **(confirm)** it keeps the front low and the footprint small.
  - Known risk from our review: a caster can drift on hard acceleration and when reversing. We are also adding an acceleration ramp, which should help.
- **Result / follow-up:** Test with the PID straight drive and yaw turns, and note any drift. If it drifts, record that here and the fix. **Square check to follow** once it is fitted: ruler flat against the back and each side, and the body should touch before any wheel (watch the front-left drive wheel). Record the result here.

## 6. Attachments (Mission 1) adapted to HummerOne's mounting bar

- **Date / who:** Status as of 2026-10-01. Sylvie, Ella, Alexis, Amelia, Brynn (the attachments group).
- **Plan:** Three Mission 1 attachment options, inspired by Giraffes #3388, Platinum Pizzeria and Team TurtleBots. Adapt each to the HummerOne bar, test all three, rate pros and cons, then pick one for final refinement.
- **Adapted so far (2 of 3):**
  - **Lifting arm, modified with a seed bucket.** The seed mission needs the seeds to go in a specific order, which Ira is writing down.
  - **2-axis attachment, modified with a hook.**
- **In progress:** **Forklift**, worked on today (2026-10-01). Robot Man's "raise the platform" mission with a forklift was Ella's first-to-implement task. The review noted the forklift is the tallest when extended and the biggest centre of gravity risk, so test it for tipping.
- **Follow-up:** Test all three on HummerOne, rate pros and cons, and record the choice as the next entry in this log with the reasoning.

## 7. Attachment pins: axle pins tried, quick pins kept

- **Date / who:** Idea from Jack, about two meetings before 2026-10-01 **(confirm date)**. Tested and reversed at the 2026-10-01 meeting.
- **Options considered:** Quick pins (what the attachments used) or axle pins to hold an attachment on the HummerOne mounting bar.
- **Why we tried axle pins:** Jack suggested them as an alternative to quick pins. **(confirm)** the benefit he had in mind, such as a smoother or faster swap.
- **What happened:** While testing the lifting arm with its new seed bucket, the attachment kept coming off with axle pins.
- **Decision:** Switched back to **quick pins, which hold more securely.** A secure fit matters more than the swap-speed idea, because an attachment that falls off mid-run loses points and time. This ties to the attachment swap speed criterion we scored (entry 2): the bar is meant to glide on and off, but it also has to stay on.
- **Follow-up:** Check the other attachments (2-axis with hook, and the forklift) for the same problem, and keep quick pins as the default. Record any swap-time measurements here.

## 8. PID drive and gyro turn My Blocks, and the Mission 2 code

- **Date / who:** Shared 2026-10-06 by **Jordan**. **Jordan and Fedor** used them in the Mission 2 code and ran test runs the same day. Code is in [mission2/](mission2/mission-2-code.md).
- **Options considered:** Driving by motor degrees only, turning by motor degrees, or the gyro (yaw) based PID drive and turns (see [mission2/mission-2-code.md](mission2/mission-2-code.md)).
- **Why:**
  - The 2026-09-29 PID sessions showed that **yaw turns the robot by a real angle**, while 90 motor degrees only turns the wheel a quarter turn. Yaw is much more accurate.
  - **`Gyro Move`** drives straight by correcting the heading error each 0.1 s: proportional (Kp 2.1) plus integral (Ki 2), with an acceleration ramp (start 15, speed up by 5, slow down by 8 at 70% of the distance). This covers the acceleration ramp and PID to-dos from 09-29.
  - **`Gyro Turn`** turns to an angle at a speed that falls as the robot nears the target (between 25 and 90 power), and stops 3 degrees early so it doesn't overshoot.
  - Both are reusable My Blocks, so every mission program can call them with a distance, a speed or an angle.
- **Result / follow-up:** Working code, and used in a Mission 2 test run. **(confirm)** the test results. Still to do: record how Jordan tuned Kp and Ki ([mission2/kp-ki-tuning.md](mission2/kp-ki-tuning.md) has the questions to ask him) and measure accuracy (drive the same distance 10 times, and 10 turns of 90 degrees). Switching turns to yaw is now done in this code. The Kp line follower is still to do.

---

## Still to record

- Why we picked each final attachment, once rated.
- Test results behind each change: ruler squaring check, drive 1 m ten times, ten 90 degree turns. Judges look for evidence of repeated testing.
- Planned changes: proportional (Kp) line follower. (Yaw turns and the acceleration ramp are in entry 8.)
