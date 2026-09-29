# Team Meeting Notes — 2026-09-29

## Bayview Glen kickoff debrief

On Sunday (2026-09-27) the team went to the FLL Challenge kickoff conference at Bayview Glen. People split up across different workshops, so today each group reported back: which workshop, who presented it, and what's useful for the team. The full transcript is in this folder, and the venue parking map is saved here too.

Most sessions were aimed at first-year teams, so a lot of it was review. The useful parts are below.

### How to Build a Functional Robot — Ira, Fedor (Fedor took notes)

Their tips:

- The robot should be able to **square up against a wall**.
- **Shield the colour sensors** from room light so they don't read the wrong thing.
- **Smaller wheels wobble less and are more accurate.** Accuracy matters more than speed.
- They showed a lot of attachments but didn't really explain them.

How HummerOne compares:

- **Front/trailing wheels:** ours have no rubber. Fedor and Ira suggest replacing them with a **ball caster**, which has almost no friction, turns best and is small.
- **Squaring:** already pretty good. The presenters' robot needed a frame around the bottom because its sensors were there. Boxed-in designs also have few places to mount attachments, and ours has good attachment points.
- **Light shielding:** fine for now. We don't use many colour sensors, and they worked when nothing was covering them.

### Programming 101 — Brynn, Amelia

- Covered the different types of blocks and the different types of turns (we only remembered three). The team mixed up the names during the debrief, so here are the standard definitions:
  - **Pivot turn:** one wheel stays still and the other drives, so the robot pivots around the stopped wheel.
  - **Point (spin) turn:** the wheels drive in opposite directions, so the robot turns on the spot.
  - **Arc turn:** both wheels go the same direction but one goes faster, so the robot drives a curve.
- Also covered using the colour sensor (mostly things we already knew).
- Main takeaway: more confidence making programming changes.
- **Rule note (Amelia):** team members *can* switch in and out at the table during a match. Last year at our tournament we were told we couldn't. Chris thinks it was that venue's first year hosting, so they may have had it wrong. Confirm in this season's rules (see Robot Game Rules below).

### Programming 201 — Jack, Jordan (presenter: Harrison)

- **Two-stage line following:** uses one colour sensor. On black, turn right; on white, turn left. The robot zigzags along the edge of the line.
- **Squaring up on a line:** needs **two colour sensors**. When one sensor (say the left) sees black, the robot turns until the other one sees black too, then wiggles until it's straight on the line.
- Why it matters: if whoever lines up the robot at a match sets it down slightly crooked, squaring up on a line or following a line fixes it automatically. Small setup mistakes stop costing us.
- Chris: there are lines right in front of several mission models that we could square up on.
- **Already acted on:** we tested in the gym and couldn't square up with only one colour sensor. After the conference **the team added a second colour sensor to the robot.**
- Jack has Harrison's email from the session if we need to follow up.

### Equity & Inclusion — Brynn, Amelia, Alexis

- They said it was really fun.
- **Helping quieter teammates be heard:** e.g. a talkative teammate notices someone with a good idea who isn't speaking up, and helps them say it.
- **Equity vs. inclusion:** inclusion means bringing everyone in and giving everyone the same. Equity means making sure each person gets what they need so everyone ends up with the same experience.
- **Dot activity:** everyone got a coloured dot on their face and had to form groups. Then they were shown pictures of circles with dots to explain each idea:
  - **Exclusion:** one colour inside the circle, all the other colours left outside it.
  - **Segregation:** each group in its own separate circle.
  - **Inclusion:** all the dots together in one circle.
- Chris: watch for these in our own day-to-day group work, and change things when we spot them.

### Robot Game & Rules Explained — Ira, Fedor, Brynn, Alexis, Amelia

**Presenter:** Jeff, head referee for provincials, who trains the referees. Chris thought his surname was "Lockheed". FIRST Robotics Canada's 2023 kickoff page lists the head referee as **Jeff Laucke**, which is probably the same person.

The session was mostly for beginners, not for provincial-level teams like us. Useful points:

- **Inspection bonus:** there are points for passing equipment inspection. Plan for it.
- **Swapping at the table:** you can swap team members at the table during a match (matches Amelia's note above).
- **Adjusting mission models:** before the match starts, you can ask the referee to adjust certain mission models that the rules allow to be moved (about 3 missions).
- **Order matters on the seed mission:** the seeds have to go in a specific order. The transcript is garbled here, so Ira should write the order down from their notes.
- **If the rules don't say you can't, you probably can.**
- **The robot is the main character:** a mission doesn't have to be done a particular way, as long as the robot follows the rules.
- **Some mission models will be randomized** at the start of a match (Brynn's notes). The transcript doesn't say which ones, so confirm from notes.
- **There was a rule change about the bugs.** Always check for rule updates. They can come out as late as ~5 days before an event, and missing one makes things harder for us.
- **Don't touch anything until the score is final.** Don't move the robot or any models until the referee has counted every point. Check the score without touching anything.
- **Don't shake the table when celebrating.** You could knock a model off and lose points.
- Amelia mentioned a mission where some pieces lose points if they get knocked down or touched. Chris doesn't think we'll attempt it. The transcript is unclear, so check the details in the rules.

Chris also mentioned Edmund Kim and the Pink Titans in connection with this session. Their role isn't clear from the transcript.

### PID — Jack, Jordan (presenter: "Mr. Pi")

- The presenter goes by Mr. Pi because he likes the number pi. He's a college teacher.
- PID makes driving straight and line following more accurate.
- **The problem:** with two-stage line following, the robot keeps turning until it sees black, so it zigzags a lot. That's slow and inaccurate.
- **The fix (proportional control):** measure how far off the line the robot is (the error) and multiply it by a small decimal number called **Kp** (e.g. 0.3). The robot turns harder when it's far off and more gently when it's close. The longer it follows the line, the closer it gets to just going straight.
- Jordan: the robot zigzags way less and goes along the line cleaner and faster.
- We already have PID material in `robot_design/` (PID_CONTROL_TUTORIAL.md, PID_TUNING_GUIDE.md, pidStraightDrive.py).

### How to Prepare for a Judging Session — Ira, Fedor (presenter: Calum Tsang)

Also mostly for first-year teams. Good tips:

- **Robot design explanation:** pick your favourite mission. Explain how you solved it, what each person did to help, and how you used your time, e.g. how we upgraded the robot or built a new one.
  - Chris: we already have upgrades to talk about from today alone: the ball caster, colour sensor shielding, and the second colour sensor for lining up.
- **Always use the rubric** (we got it last year) to see how judges score and how to score the most.
- **Describe how we did things in detail, step by step.** This goes for core values and for code: walk through it step by step.
- **Be nice:** be encouraging to other teams and to our own team, and thank the judges on the way out.
- Direct quote: **"Don't trust AI."** Start with Google and real sources.
  - Chris: last year, whenever we got an answer from AI we checked the source. We'll do that again this year.

### FIRST Like a Girl — Brynn, Amelia

- FIRST Like a Girl is about empowering women and girls in STEM. It's an outreach program run by FRC Team 1902 **Exploding Bacon** from Orlando, Florida. Their logo is a pig on a rocket ship with fire coming out.
- It wasn't really about robots, but they learned things about FIRST, and there was trivia, e.g. about Marie Curie and her discovery of radioactivity.
- They also learned about **ConnecTech**, an FLL team with a YouTube channel, a website, Instagram and Facebook.
- Chris: add ConnecTech and FIRST Like a Girl to our team resources, and research both to see what we can learn.

### Programming 301 — Jack

- **Acceleration ramp:** the robot starts slow, speeds up, then slows down again before it stops. This is more accurate than going full speed right away.
- **Yaw (gyro) turns:** instead of telling a wheel motor to turn 90°, tell the robot to turn to 90° of **yaw**. If the turn is a little off, the gyro sensor corrects it.
  - **Yaw 90° vs. motor 90°:** yaw works like a compass, so the *robot* turns 90°. On the motor, a full wheel rotation is 360°, so 90° only turns the *wheel* a quarter turn, not the robot. That's much less accurate.
- **PID in code:** the PID session explained what PID is. In 301 they learned how to use PID in code to follow lines and drive straight.

## Innovation project kickoff

For the rest of the meeting (~half an hour) the team brainstormed innovation project ideas.

- **Today's goal:** a **topic** plus a **guess at a specific problem** within it. It doesn't have to be a proven problem yet.
- **Example (Amelia):** topic *invasive species*. The problem: they eat the food native animals need, and native animals die off, which reduces biodiversity.
- **Format:** small groups or individuals write down 3–5 topic + problem ideas, 15–20 minutes.
- **By next Tuesday (2026-10-06):** research the topics and use sources to prove each problem really is a problem. If AI gives us an answer, check its source (see judging tips above).

The list of ideas the groups came up with isn't in the transcript. Add them here or in `innovation_project/`.

## Action items

**Robot**
- [ ] Replace HummerOne's rubber-less front/trailing wheels with a ball caster
- [ ] Program square-up on a line using the new two colour sensors
- [ ] Find the lines in front of mission models we can square up on
- [ ] Switch turns to yaw (gyro) turns instead of motor-degree turns
- [ ] Add an acceleration ramp (start slow, speed up, slow down) to drive moves
- [ ] Build a proportional (Kp) line follower and tune Kp, using the PID material in `robot_design/`

**Robot game / rules**
- [ ] Read this season's rules and confirm: table swaps, which mission models the ref can adjust before the match, the inspection bonus, the bugs rule change
- [ ] Write down the correct seed order for the seed mission (Ira)
- [ ] Check for rule updates regularly, and always in the week before any event
- [ ] Practise match-end habits: nobody touches the robot, models or table until the score is final

**Judging**
- [ ] Find last year's judging rubric and keep it handy for robot design and innovation
- [ ] Start a robot design log: each upgrade (ball caster, second colour sensor, etc.), who did it, and why. Include why we picked HummerOne (carried over from 2026-09-22)

**Innovation project**
- [ ] Add today's brainstormed topics and problems to the notes
- [ ] Research the topics and back up each problem with real sources, due 2026-10-06

**Resources**
- [ ] Research ConnecTech and FIRST Like a Girl: find their links and what we can learn from them

Done since last meeting: added a second colour sensor to the robot after testing in the gym showed we couldn't square up with one.
