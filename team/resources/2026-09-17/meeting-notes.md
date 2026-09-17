# Team Meeting Notes — 2026-09-17

## Bot-fluencers presentations

More Bot-fluencer presentations today. Full details tracked in the running list: [../bot-fluencers.md](../bot-fluencers.md).

| Presenter | Bot-fluencer | First to implement |
|---|---|---|
| Fedor, Ira | Platinum Pizzeria | Build a passive attachment for Mission 1 |
| Jack | Mocking Bricks | Check out the line following video |
| Ella | Robot Man | Try the "raise the platform" mission with a forklift |

Links (YouTube channels, website, and the specific line-following video) are still TBD — see the TODO markers in [../bot-fluencers.md](../bot-fluencers.md).

## Workstreams

The team split into four workstreams. Three groups each build a Mission 1 attachment from a different bot-fluencer, and one group builds the starter bot they will all mount on.

| Group | Working on | Inspiration |
|---|---|---|
| Sylvie, Brynn, Jack | Starter bot | Next Level Teacher (HummerOne) + Robotics Rules (Starter Bot) |
| Amelia, Ella | Mission 1 attachment | Giraffes #3388 |
| Fedor, Ira | Mission 1 attachment | Platinum Pizzeria |
| Jordan, Alexis | Mission 1 attachment | Team TurtleBots |

## The plan

1. Build the starter bot.
2. Once the starter bot exists, adapt each of the three Mission 1 attachments to fit it.
3. Test all three attachments on the starter bot and rate them with pros/cons.
4. Pick one attachment for final refinement.

## Starter bot research

Web research on the bot-fluencers' starter bot resources (only two of the four actually have one):

**Robotics Rules — "Starter Bot"** (strongest option)
- Page: https://www.roboticsrules.net/starter-bot
- Built entirely from one SPIKE Prime set (45678); 18×19 LEGO units; centre of gravity near the front so it doesn't tip; gear-based attachment mount for quick swaps. One set gives "enough pieces for the Starter Bot and 2–3 attachments."
- Attachment library: horizontal/vertical circular, horizontal/vertical rack & pinion, basic attachment.
- Cost: StarterBot Instructions v1.3 (Sept 2026) is **$30** in the shop (https://www.roboticsrules.net/category/all-products). Passive Attachment Designs $10, One-Way Door $5, FLL Masher instructions free.
- Free supporting pages: Building Tips (https://www.roboticsrules.net/building-tips) and Coding Strategies (https://www.roboticsrules.net/coding-strategies — covers SPIKE and PyBricks).

**Next Level Teacher — "HummerOne"**
- The free FLL FastTrack course (https://nextlevelteacher.com/product/fll-fasttrack/) has a Robot Design section with "HummerOne Building Instructions" plus Attachment 1/2/3 lessons. Requires (free) enrolment to view.
- The standalone HummerOne course (https://nextlevelteacher.com/courses/hummerone/) is currently closed for enrolment.

**Team TurtleBots** — no starter bot content; Robot page is competition recordings. Maker Shop advertises "Free FLL Resources" via Zeffy (https://www.teamturtlebots.org/maker-shop) — someone should click through and see what's there.

**Giraffes #3388** — no build instructions. Their robot design post (https://giraffesaimhigh.com/submerged-robot-design/) describes a compact 12×15 unit robot with colour-coded attachments for automatic run detection, plus trapezoidal motion profiling and PID (see our own `robot_design/` PID code).

**Free alternatives if we don't want to spend $30**
- PyBricks SPIKE Prime StarterBot — free 26-step build from one 45678 set: https://pybricks.com/learn/building-a-robot/spike-prime/
- FLL Tutorials "How to Build an FLL Base Robot" video: https://www.youtube.com/watch?v=48gC-E2aaRA

Note: YouTube blocks automated browsing of channel video lists, so the channel videos themselves still need a manual look.

## Action items

- [ ] Starter bot group: enrol in the free FLL FastTrack course and review the HummerOne build; decide whether the $30 Robotics Rules StarterBot instructions are worth buying (coach decision)
- [ ] Someone check the TurtleBots Maker Shop free resources
- [ ] Still need YouTube links for Platinum Pizzeria, Mocking Bricks, Robot Man (see bot-fluencers.md)
