# Robot Design Review — Tournament Performance Perspective

Reviewed 2026-09-21, revised with Comp Bot added and the GummyBears / Droid Bot M designs merged.
Source files: `team/resources/build instructions/`, plus the Robotics Rules StarterBot (evaluated from public material only).

This review scores each base robot on how it is likely to perform **in a tournament match** — 2.5 minutes, repeated launches from home, attachment swaps under time pressure, and a Robot Design judging session — rather than on how nice the instructions are.

**Method and its limits.** The PDFs are image-only booklets, so the design assessment comes from cover art, parts lists, part-completion pages and final-assembly pages. StarterBot has no PDF; it was assessed from its creator's public videos and website. I could not watch competition gameplay footage, so where I say a design "matches what wins," that means archetype match against the documented competitive shape described by FLLCasts, the Seshan Brothers' competition-robot guide and Roboplex's chassis guide — not a count of robots in videos.

**Two designs have been merged.** GummyBears and Droid Bot M share the same drivetrain construction and produce near-identical robots; the differences are too small to justify separate entries. They are scored as one design below. Earlier versions of this review scored them apart and quite differently, which was over-reading two fixed render angles rather than seeing a real difference.

---

## The archetype these get scored against

Published competitive guidance converges on a fairly narrow robot shape:

- **Compact rectangular "box" chassis**, roughly 15–18 LEGO units per side. Small footprint means easier navigation between mission models and less launch-area congestion.
- **Two drive wheels near the center of mass**, hub mounted low and flat. Turns become rotations about a predictable point, which is what makes gyro turns and PID drive repeatable.
- **Low center of gravity**, because CG shifts when the robot picks up game pieces, and top-heavy robots skid and veer on turns.
- **A flat, full-width attachment surface** so attachments glide on and off. A robot that takes 15 seconds to change tools has lost 10% of the match.
- **Flat back and flat sides for squaring.** One of the highest-value features on the whole robot. Flat faces let you push the robot against the launch-area walls to square it, giving an identical starting position every run without measuring, and let it re-square against a field wall mid-run to cancel accumulated heading error. The flat faces must be the **widest** part of the robot — a round tire protruding past the body touches a wall at one tangent point and pivots instead of squaring.
- **Minimal part count**, for reliability.

Judging note: the official Robot Design rubric scores mission strategy, use of building resources, explanation of attachments, and evidence of repeated testing. Nothing penalizes a team for starting from a published base — "clear use of building or coding resources to support their mission strategy" is explicitly an accomplishment marker. Judges will ask *why this base* and *what you changed*.

---

## Base robot designs

### 1. Comp Bot — `comp bot.pdf`
*Zain Khan ("Coach Zain") — free PDF, linked from [5 Simple Tips to Build the Ultimate FLL Robot](https://www.youtube.com/watch?v=4aHr97Xof34)*

**Tournament summary.** A fully enclosed box robot, and the most single-mindedly competition-focused design of the four. 225 steps in four parts: drivetrain (1–35), attachment motors (36–51), hub (53–65) and framing (67–225). That last number is the story — **158 of the 225 steps are frame**. The finished robot is a solid rectangular shell with the drive wheels completely inside it, the hub recessed into the top surface, and two attachment motors with dog-gear outputs poking up through the deck.

The design philosophy is stated outright in the source video: choose components deliberately, build outward from the drivetrain, stabilise, **build a frame around the robot**, and **use dog gears** for attachment coupling.

**Reach.** The source video has ~91K views over five years, against ~4.7K for StarterBot's flagship. Of everything here this is the design most likely to have been built by large numbers of teams — though that's view count, not a count of robots on competition tables.

**Performs well in a match because:**
- **Best squaring of any design here, by construction.** The frame encloses the robot on all four sides and the wheels sit entirely inside it, so the flat faces *are* the widest surfaces — there is nothing to protrude and spoil the contact. Push it against a wall from any face and it squares. This is the single feature that most improves run-to-run consistency, and no other design here achieves it as cleanly.
- **Most rigid chassis by a wide margin.** 158 steps of framing means effectively zero flex, and chassis flex is a silent, hard-to-diagnose source of drive inaccuracy.
- **Two dedicated attachment motors with dog-gear couplings.** Dog gears engage without needing precise meshing, so attachments drop on and drive immediately. And two motors means some mission pairs can run without swapping at all — the fastest swap is the one you don't do.
- Low, enclosed, protected. The hub is recessed, so knocks in the pit don't disturb anything.
- Free, with no signup or paywall.

**Costs you in a match:**
- **Biggest and heaviest of the four.** Worst maneuverability in tight mission clusters, slowest acceleration, longest stopping distance, most battery draw.
- **225 steps** — roughly three times HummerOne and seven times the merged GummyBears build. This is several meetings of work before any mission testing starts.
- **Four motors** (two drive, two attachment) likely exceeds a single SPIKE Prime core set. Check inventory before committing; this may be the deciding practical constraint.
- The enclosed frame makes internal access harder. Swapping a motor or re-routing a cable mid-season means taking the shell apart.

### 2. HummerOne — `HummerOne.pdf`
*Next Level Teacher — free via the FLL FastTrack course (free enrollment required)*

**Tournament summary.** A boxy perimeter frame with two rear drive wheels, a front support wheel, and a full-width attachment bar across the top front. Explicitly built and marketed as an FLL competition robot with modular attachments designed to come on and off quickly.

**Competition provenance: unverified.** Described by its creator as "specially designed for competing in FLL," but no public tournament results tie to it, and the instructions sit behind a course login.

**Performs well in a match because:**
- **Fastest attachment handling of the four.** The full-width bar lets attachments glide on and off rather than being pinned piece by piece — the difference between a five-second swap and a twenty-second one.
- Reinforced box frame, second only to Comp Bot for rigidity and stability under attachment load.
- The magenta perimeter frame gives genuine flat side and rear panels, good for squaring — though check whether the front-left drive wheel sits proud of the frame.
- Video build support and coding lessons, so a stuck subteam can unblock itself without the coach.
- The four attachment PDFs already in this folder share its conventions and fit without rework. Convenient, though not decisive — attachment designs are plentiful online and the subteams are working from Giraffes #3388, Platinum Pizzeria and TurtleBots designs anyway.

**Costs you in a match:**
- Heavy and bulky. Second-worst maneuverability.
- 73 steps — moderate, but still a meeting or two.

### 3. StarterBot — *(no PDF in the folder)*
*Robotics Rules — instructions $30; assessed from public videos and site material*

**Tournament summary.** A compact 18 × 19 stud robot built from one SPIKE Prime set, with an unusually well-thought-out attachment system: attachments couple through **gears**, and a color sensor **identifies which attachment is fitted** so the robot runs the matching code automatically, keeping all mission code in one program.

**One design choice worth flagging:** the center of gravity is deliberately biased **toward the front** to resist tipping. Most guidance puts the CG near the drive wheels, so this is a considered trade rather than a standard approach.

**Performs well in a match because:**
- Gear coupling plus color-sensor identification removes the "scroll through program slots" step at base entirely.
- Best archetype match alongside Comp Bot — compact, one set, purpose-built.
- Best maneuverability of the top three.
- The free supporting videos (center of gravity, precision turning, MyBlocks, attachment coding) carry real design reasoning, and the Coding Strategies page covers PyBricks as well as SPIKE.

**Costs you in a match:**
- **Weak on squaring — the sides are not flat.** The creator advertises "easy alignment" front-facing and rear-facing along the field side wall, but without flat sides that claim doesn't translate into square-and-go behaviour. Treat it as a marketing bullet, not a measured result.
- The gear mounting is its own interface, so attachments have to be built for it.
- Current revision costs $30; the free live-build video shows the older pre-update design.
- Build length unknown from public material, so it can't be planned against.

### 4. GummyBears / Droid Bot M — `fllrobotjan2025.pdf`, `DroidBotMSpikePrime.pdf`
*GummyBears Robotics (FLL Team #44355) and Sanjay & Arvind Seshan (PrimeLessons) — both free*

**Tournament summary.** Two published builds that share a drivetrain construction and produce near-identical robots: a compact chassis with two large drive wheels, the hub low, and a third point of contact at the rear. GummyBears adds a wider front pin rail; Droid Bot M uses a smaller dedicated attachment module. Scored together because on the mat they behave the same.

**Provenance is strong on both counts.** The Gummy Bears won the **FIRST Championship World Festival 2022 Robot Design Award**; the Seshan Brothers run the most widely distributed free FLL resources in the world. Worth knowing that PrimeLessons classifies Droid Bot M as a **training robot**, pointing to Droid Bot E and Droid Bot IV as its competition designs.

**Performs well in a match because:**
- Compact and light — the best maneuverability of the four, and the quickest to accelerate.
- **Much the fastest build here** (roughly 31–39 steps against Comp Bot's 225), so the team gets to driving, coding and testing soonest. Testing time is what the rubric actually rewards.
- Free and unrestricted.
- The GummyBears variant's front pin rail gives all three attachment subteams a common mounting standard.

**Costs you in a match:**
- **Weakest squaring of the four.** The drive wheels look like the widest point on both variants, so there may be no flat face that can reach a wall. Confirm with a ruler before committing — this is the fix-it-or-live-with-it decision for this design.
- Attachment mounting is pin- or module-based, no quicker at base than any other pinned design.
- The rear caster/ball is a drift risk on hard acceleration and reversing.
- Higher center of gravity than the framed designs, so less planted once an attachment extends forward.
- Droid Bot M additionally needs expansion-set parts (extra large motor, color sensor, ball wheel, frame).

---

## Scoring for tournament use

Rated 1–5 for competition impact; higher is better.

| Criterion (match impact) | Comp Bot | HummerOne | StarterBot | GummyBears / Droid Bot M |
|---|---|---|---|---|
| Archetype match to proven competitive designs | **5** | 4 | 5 | 4 |
| Attachment swap speed at base | **5** (dog gears, 2 attachment motors) | **5** (full-width glide-on bar) | 4 (gear coupling + auto-ID) | 3 |
| **Squaring — flat back and sides for wall alignment** | **5** (enclosed frame, wheels internal) | 4 (perimeter frame panels) | 3 (sides not flat) | 2 (wheels are widest point) |
| Stability / tipping resistance under load | **5** | 5 | 4 | 3 |
| Maneuverability in tight mission areas | 2 | 2 | 4 | **4** |
| Drive repeatability (for our PyBricks PID code) | 4 | 4 | 4 | 4 |
| **Total (out of 30)** | **26** | 24 | 24 | 20 |

**This is a pure on-field performance matrix.** Criteria dropped from earlier versions, and why:

*Source pedigree* — a fact about the author, not the robot, and archetype match already covers whether a design is competitive. Provenance stays in the write-ups as context, because it calibrates how much to trust an unverified claim.

*Compatibility with the four attachment PDFs on hand* — attachment designs are abundant online, so fitting those particular four was never a real constraint.

*Fits one core set, build time cost, access* — real constraints, but logistics rather than performance. They describe what it costs to obtain and build a robot, not how it behaves in a match. They belong in the judgement after the scoring, not inside it.

Squaring scores are read off 3D renders, so treat them as provisional for every design except Comp Bot, where the enclosed frame makes the answer unambiguous. The definitive test takes five minutes: sit the built robot on a table and push a ruler flat against each face in turn, checking whether the body contacts flush or a wheel, pin or caster touches first.

---

## Attachment mechanisms, by mission capability

These mount on a base; they aren't base alternatives.

| Attachment | Build cost | Match capability | Tournament caution |
|---|---|---|---|
| **Multipurpose Single** | 9 pg | Single-point paddle/flipper. Fastest route to a working Mission 1 tool. | One simple motion; will be outgrown |
| **2-Axis Movement** | 13 pg | Bevel gears give vertical + horizontal motion from one input — two mission actions, saving a swap | Gear backlash reduces precision |
| **Lifting Arm** | 15 pg | Geared hinge arm for scoop/hook missions | Watch forward CG shift |
| **Forklift** | 73 pg, 3 phases | Rack-and-pinion vertical lift for platform missions | Tall when extended; biggest CG risk |

---

## Recommendation

**On performance, Comp Bot wins at 26 of 30, and it wins on the right things.** It is the only design that solves squaring completely — the frame encloses the wheels, so the flat faces are the widest surfaces and the robot squares against a wall from any side. Add the most rigid chassis here, two attachment motors with dog-gear couplings, and the widest apparent adoption of any source in this review, and it is the strongest competition robot of the four. It is also free.

**Its cost is time and parts, and both are real.** 225 steps is several meetings, and four motors probably means more than one core set. Neither is a performance problem, but either could be a season-planning problem. Check the motor inventory first — if the team doesn't have four motors, this decision is already made.

**HummerOne and StarterBot tie at 24** and are the sensible middle ground. HummerOne is the better of the two here: same score, but free through the FastTrack course where StarterBot's current revision costs $30, a quarter of Comp Bot's build length, and no unverified claim propping up its score. If Comp Bot's build length or motor count rules it out, build HummerOne.

**GummyBears / Droid Bot M at 20 is the fast option, not the strong one.** Merging the two removed the inflated score the GummyBears variant was carrying, and what's left is a light, nimble, quick-to-build robot with the weakest squaring of the group. That last point is the one to weigh: if the wheels really are the widest surface, every launch starts from a slightly different place all season. It remains the right choice if meeting time is genuinely scarce — and an excellent training platform for getting the PyBricks PID code running while a better chassis is built alongside.

**Whatever wins, fix the squaring before mission work starts.** If the chosen chassis doesn't present flat faces as its widest surfaces, it is usually a cheap fix — a beam or two run flush along each side and the rear, standing slightly proud of the wheels, converts a mediocre squaring robot into a good one. Far cheaper than discovering in February that every run starts differently.

**One idea worth stealing regardless of base:** the color-sensor attachment identification technique is free, design-independent and well documented by Robotics Rules. Keeping all mission code in one program and letting the robot detect its own attachment is a clean win for pit speed, and a good thing to explain to judges.

Starting from a published base is not penalized in judging — but the team needs to say why they chose it, what they tested, and what they changed. Credit the source either way.

---

## Sources

- [5 Simple Tips to Build the Ultimate FLL Robot — Zain Khan](https://www.youtube.com/watch?v=4aHr97Xof34)
- [DroidBot M SPIKE Prime — FLL Tutorials](https://flltutorials.com/en/robotgame/building/one%20kit%20build/2020/07/06/DroidBotMSP.html)
- [Robot Designs — PrimeLessons](https://primelessons.org/en/RobotDesigns.html)
- [Building a Competition Robot — Seshan Brothers](https://flltutorials.com/translations/en-us/RobotGame/FLLRobot.pdf)
- [SPIKE Prime Box Robot — FLLCasts](https://www.fllcasts.com/materials?construction_designs=box-robots&in_categories%5B%5D=29&pref_order=latest)
- [Chassis Design for FLL — Roboplex](http://roboplex.org/wp/wp-content/uploads/2015/10/Chassis-Design-FLL-2017.pdf)
- [FLL Challenge Robot Design rubric (Submerged)](https://firstinspires.blob.core.windows.net/fll/challenge/2024-25/fll-challenge-submerged-rubrics-color.pdf)
- [Gummy Bears FLL webinar — SOLIDWORKS Education blog](https://blogs.solidworks.com/teacher/2022/09/first-lego-league-fll-informational-webinar-from-the-gummy-bears.html)
- [How to Build an FLL Base Robot — GummyBears Robotics](https://www.youtube.com/watch?v=48gC-E2aaRA)
- [HummerOne — Next Level Teacher](https://nextlevelteacher.com/courses/hummerone/)
- [Starter Bot — Robotics Rules](https://www.roboticsrules.net/starter-bot)
