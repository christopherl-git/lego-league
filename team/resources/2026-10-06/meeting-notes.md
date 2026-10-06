# Team Meeting Notes — 2026-10-06

## Innovation project topic presentations and vote

Each team member presented a topic, the problem within it, and a source. The team then voted on one topic (top three choices each, 3/2/1 points). Details and observations are in [innovation_project/topic-vote-2026-10-06.md](../../../innovation_project/topic-vote-2026-10-06.md) and the ballots are in [innovation_project/topic-vote-tracker.xlsx](../../../innovation_project/topic-vote-tracker.xlsx).

| Presenter | Topic | Problem | Source |
|---|---|---|---|
| Alexis | Ocean acidification | Harms coral reefs and marine animals | NOAA |
| Amelia | Animals in captivity | Zoochosis, reduced biodiversity | In Defense of Animals, World Animals Protection |
| Sylvie | Human-made wildfires | Habitat burned, animals killed | CBC |
| Ella | Pollution | Habitat loss | None |
| Brynn | Light pollution | Turtles and moon-following animals can't navigate | None |
| Jack | Invasive species | Harms native species, reduces biodiversity | None |

**Winner: invasive species (Jack).** Jack's topic had no source yet, so finding a credible one is the first task. Pollution and light pollution also came without sources.

## Jordan shared working PID drive and turn My Blocks

Jordan shared functioning **PID drive** and **PID turn** My Block code. This is the PID work from the 2026-09-29 conference (drive straight and turn accurately using feedback) now running on the robot. The code isn't in the repo yet; see the action items.

## Breakout groups

- **Jordan and Fedor:** worked on the code for Mission 2 and ran some test runs. The code is saved at [robot_design/mission2/](../../../robot_design/mission2/mission-2-code.md): it drives and turns with Jordan's PID `Gyro Move` (Kp 2.1, Ki 2) and `Gyro Turn` blocks.
- **Jack and Ira:** continued working on the forklift attachment (third Mission 1 attachment, adapting it to HummerOne's mounting bar).
- **Ella, Amelia and Alexis:** group research on the innovation topic.
- **Sylvie and Brynn:** group research on the innovation topic.

## Action items

- [ ] Find a credible source (ideally Canadian: government or university) showing invasive species harm native species and biodiversity — Jack
- [ ] Narrow invasive species to one specific problem we could design a solution for
- [ ] List experts to contact (conservation authority, researchers, local invasive species groups)
- [x] Jordan's PID drive and turn My Block code saved in `robot_design/mission2/`
- [ ] Document how Jordan tuned Kp and Ki (starting values, what he changed, what each change did): answer the questions in [robot_design/mission2/kp-ki-tuning.md](../../../robot_design/mission2/kp-ki-tuning.md) — Jordan
- [ ] Write up what happened in the Mission 2 test runs (what worked, what failed, what to change next) — Jordan, Fedor
- [ ] Test the PID drive and turns on HummerOne and record how accurate they are (distance and turn error)
- [ ] Finish adapting the forklift to HummerOne's mounting bar — Jack, Ira
