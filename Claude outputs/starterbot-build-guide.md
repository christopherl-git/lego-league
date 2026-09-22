# StarterBot — Build Guide & Session Plan

**Team:** Look it's a Giraffe! · **Workstream:** Starter bot (Sylvie, Brynn, Jack)
**Design credit:** Robotics Rules — https://www.roboticsrules.net
Prepared 2026-09-21. This is our working guide, not a substitute for the creator's instructions.

---

## The source material

Everything below points at Robotics Rules' own material. Watch these in order — the first two are the ones that matter for building.

| Video | Length | Why watch it |
|---|---|---|
| [StarterBot — The AWESOME robot system for novice and rookie FLL teams](https://www.youtube.com/watch?v=oZh5O4pW1y4) | 12:22 | The design overview. Eight specific claims about why it works, all listed below. Watch this first. |
| [StarterBot for Rookie and Novice FLL teams — Live Build](https://www.youtube.com/watch?v=niSTzqKErSY) | 5:54 | **The build walkthrough.** Whole robot, one SPIKE Prime set. Condensed, so expect to pause and scrub constantly. Shows the pre-update revision. |
| [FLL StarterBot UPDATE](https://www.youtube.com/watch?v=IUt1MLcNirg) | 3:39 | Describes a design change that makes it easier to build extensions onto attachments. This change is **not** in the live-build video. |
| [Save Time and Effort with the FLL Color Sensor Attachment System](https://www.youtube.com/watch?v=KliqWvv_AVs) | 9:02 | Full coding walkthrough for attachment auto-identification. Useful on any robot, not just this one. |
| [Center of Gravity — The Key To Building an Effective FLL Robot](https://www.youtube.com/watch?v=vVthicvuX3w) | 10:43 | The reasoning behind StarterBot's front-biased CG, including a motor-placement experiment. |
| [Turning your FLL robot with PRECISION](https://www.youtube.com/watch?v=fBLGj_lOd7M) | 14:10 | Pairs with our PID work in `robot_design/`. |

**Reference pages:** [Starter Bot](https://www.roboticsrules.net/starter-bot) · [Building Tips](https://www.roboticsrules.net/building-tips) · [Coding Strategies](https://www.roboticsrules.net/coding-strategies) (covers PyBricks, not just SPIKE)

### Free vs. paid

| Item | Cost |
|---|---|
| All videos above | Free |
| Building Tips / Coding Strategies pages | Free |
| **FLL Masher instructions (June 2026 V1)** | **$0.00 — download this** |
| StarterBot Instructions v1.3 (Sept 2026) | $30 |
| Passive Attachment Designs | $10 |
| One-Way Door Instructions | $5 |

The Masher is a StarterBot attachment and it's a free download, so it's the cheapest way to see how the gear-based mounting interface actually works before deciding on the $30 manual.

---

## What the design claims

From the creator's own overview video — these are the things to verify once we've built it:

1. **One set.** Builds entirely from a single LEGO Education SPIKE Prime Set (45678). No expansion parts.
2. **Versatile attachments.** Supports circular motion horizontal and vertical, lateral motion horizontal and vertical, and passive attachments.
3. **No gear slipping.** Attachments couple through gears, so power transfers reliably from the attachment motor.
4. **Small footprint.** Approximately 18 × 19 studs.
5. **Stable design.** Built to resist wobbling during operation.
6. **Strong traction.** Grips the field well enough to drive straight and turn at high speed without wheel slip.
7. **Easy alignment.** Squares against the field side wall both front-facing and rear-facing.
8. **Color sensor attachment ID.** The robot reads which attachment is fitted and runs the matching code automatically.

**The unusual one:** the center of gravity sits near the **front** of the robot, which the creator says stabilizes it and prevents tipping during missions. Most FLL guidance puts the CG near or between the drive wheels, so this is a deliberate trade tied to their attachment style. Don't assume it — test it.

**Treat claim 7 with caution.** Squaring against a wall is how you get an identical starting position every run without measuring, and how you cancel accumulated heading error mid-sequence — so "easy alignment" sounds like a headline feature. But proper squaring needs flat faces that are the *widest* part of the robot, and StarterBot's sides are not flat. Anything protruding (an outboard wheel, a stray pin) means the robot touches the wall at a single point and pivots instead of squaring. Whatever method the creator demonstrates, it isn't flush body contact along the side. The flat face audit in the test table below is how we find out what it actually gives us — run it before trusting the claim.

---

## Before the build session

- [ ] Confirm we have a complete, sorted SPIKE Prime 45678 set. Nothing else is needed.
- [ ] Hub charged and firmware current.
- [ ] Decide the manual question: buy v1.3 for $30, or build from the live-build video knowing it's the older revision. (Coach decision — see note at the end.)
- [ ] Download the free Masher instructions so we can see the attachment interface.
- [ ] Whole workstream watches the 12:22 overview video together before touching bricks.
- [ ] Someone assigned to photograph our build at each stage (see below).

---

## Build session plan

**Session 1 — understand before building (30 min)**
Watch the overview video as a group. Each person writes down one thing they expect to be good about this design and one thing they're unsure about. Keep these — they become judging answers later.

**Session 2 — build (est. 60–90 min)**
Build from whichever instructions we've chosen. Working rules:
- One person drives the instructions, two build. Rotate every 15 minutes so everyone touches the robot.
- Stop at any point where the video is ambiguous and note the timestamp rather than guessing. Collect the ambiguities; don't let one stall the session.
- Photograph each major sub-assembly as it's finished (see the log below).

**Session 3 — verify the claims (45 min)**
Run the tests in the next section. Record real numbers. This is the part judges care about most, and it's the part teams usually skip.

---

## Verification tests

Each of these checks one of the design's claims. Record the result — this table is our evidence for Robot Design judging.

| Test | How | Target | Result |
|---|---|---|---|
| Footprint | Measure length × width in studs | ~18 × 19 | |
| Center of gravity | Balance the robot on a finger/edge, mark where it balances | Forward of the wheel axis | |
| CG with attachment | Repeat with the heaviest attachment fitted | Still stable, no tipping | |
| Straight-line drive | Drive 1 m at high speed, measure drift | < 2 cm | |
| Turn repeatability | Ten 90° gyro turns, measure final heading error | < 3° | |
| **Flat face audit — rear** | Push a ruler flat against the back. Does the body contact flush, or does a wheel/pin/caster touch first? | Body contacts flush | |
| **Flat face audit — left side** | Same, left side | Body contacts flush | |
| **Flat face audit — right side** | Same, right side | Body contacts flush | |
| Wall alignment, front | Square against side wall front-facing, drive off, repeat ×5 | Same position each time, < 1 cm spread | |
| Wall alignment, rear | Same, rear-facing, ×5 | Same position each time, < 1 cm spread | |
| Attachment swap time | Time a full swap, hands-on-robot to ready | < 5 s | |
| Battery behaviour | Repeat straight-line test at low battery | Drift unchanged | |

---

## Coding notes

Two things tie directly into work we already have:

**PID drive.** We already have `robot_design/pidStraightDrive.py` and the tuning guide. The StarterBot's strong-traction claim should make PID tuning easier, not harder — less slip means the encoder count matches actual distance travelled. Re-tune from scratch on this chassis regardless; our current constants were tuned on a different robot.

**Color sensor attachment ID.** This is worth adopting whichever base we end up with. The idea: put a distinctly coloured element on each attachment, have the robot read it on startup, and branch to that attachment's routine. Benefits are all code in one program instead of a pile of slots, and no scrolling through program slots at base during a match. The [walkthrough video](https://www.youtube.com/watch?v=KliqWvv_AVs) covers it step by step in SPIKE; translating it to PyBricks is straightforward and would be a good task for whoever wants a coding challenge.

---

## Our build photo log

Rather than working from someone else's images, we take our own as we build — it gives us reference shots at exactly the angles we need, and photographic evidence of our process is directly useful in Robot Design judging.

Take each shot on a plain surface with good light. Save to `team/resources/build instructions/starterbot-photos/`.

| # | Shot | Taken by | Date |
|---|---|---|---|
| 1 | Sorted parts before starting | | |
| 2 | Drive assembly — top | | |
| 3 | Drive assembly — underside | | |
| 4 | Drive assembly — both sides | | |
| 5 | Hub mounted, front | | |
| 6 | Hub mounted, rear | | |
| 7 | Attachment gear interface, close up | | |
| 8 | Color sensor position, close up | | |
| 9 | Finished robot — front, rear, both sides, top, underside | | |
| 10 | Finished robot with an attachment fitted | | |

Shot 7 matters most. If we ever need to rebuild or repair mid-tournament, the gear interface is the part nobody will remember.

---

## Open questions for the team

- Do we buy the $30 v1.3 manual? Arguments for: it's the current revision, it includes the attachment-extension fix the free video predates, and it directly supports a creator whose free material we're already using heavily. Against: the GummyBears base is free and has a stronger competition record, and StarterBot's gear mounting doesn't fit any of the four attachment builds we already have.
- If we adopt StarterBot, the three Mission 1 attachment subteams need to rebuild to the gear interface. Is that a reasonable ask this far into the season?
- Either way: should we adopt the color-sensor attachment ID technique on whichever base we pick? (My read: yes.)

---

*Robot design credit: Robotics Rules (roboticsrules.net). LEGO®, SPIKE™ and FIRST® LEGO® League are trademarks of their respective owners; Robotics Rules is an independent resource not affiliated with either.*
