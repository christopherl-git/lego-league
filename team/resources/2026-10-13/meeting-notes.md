# Team Meeting Notes — 2026-10-13

## Jordan's weekend work: Missions 2 and 11, front support, Gyro Move in cm

Jordan showed what he did over the weekend.

### Code progress on Mission 2 and Mission 11

Jordan made progress on the code for **Mission 2** (started with Fedor on 2026-10-06) and **Mission 11**. The new code isn't in the repo yet; see the action items.

### Front support: mine cart wheels replaced with a Technic ball joint

Jordan switched HummerOne's front support from the mine cart wheels to a **Technic ball joint**. This is the low-friction support we planned as the mini ball caster (design log entries 3 and 5).

| | Mine cart wheels | Technic ball joint |
|---|---|---|
| Driving straight | Very good | Good after retuning (see below) |
| Turning | Resistance when turning | Better for turns |
| Fit | Stuck out past the sides of the robot | Stays under the robot |

Because the ball joint stays under the robot, the sides are clear for squaring against a wall. The ruler squaring check is still to do.

### Kp and Ki retuned after the switch

The ball joint introduced some **wobble** when driving straight, so Jordan had to adjust **Kp and Ki** to make the robot go straight again. The new values aren't recorded yet. The 2026-10-06 values were Kp 2.1 and Ki 2 (see [kp-ki-tuning.md](../../../robot_design/mission2/kp-ki-tuning.md)).

### Gyro Move now takes centimetres instead of degrees

Jordan changed the `Gyro Move` My Block so the distance is given in **cm** instead of motor degrees. This makes it easier to talk about a mission ("drive 30 cm") and to test it with a ruler on the table.

**Conversion: 2070 motor degrees = 100 cm**, measured with a 1 m measuring stick. That is **20.7 degrees per cm**.

The Mission 2 distances, which were in motor degrees (140 and 625), have been converted to cm. At 20.7 degrees per cm they come to about 6.8 cm and 30.2 cm.

## Breakout groups

- **Jordan, Brynn and Jack:** built an attachment to catch the seed on **Mission 11**. They built a basket, but sometimes the seed went over the top of it.
- **Ella and Amelia:** worked on the forklift build.
- **Fedor, Alexis and Sylvie:** looked for credible sources for the innovation project (invasive species).

## Action items

- [ ] Save the updated Mission 2 and Mission 11 code to the repo (`robot_design/`) — Jordan
- [ ] Record the new Kp and Ki values after the ball joint switch, and what the wobble looked like before retuning (add to [kp-ki-tuning.md](../../../robot_design/mission2/kp-ki-tuning.md)) — Jordan
- [x] Measure the cm conversion for `Gyro Move`: 2070 degrees = 100 cm (20.7 degrees per cm), tested with a 1 m measuring stick
- [x] Convert the Mission 2 distances from motor degrees to cm
- [ ] Test the PID drive on HummerOne with the ball joint: drive the same distance 10 times and measure the spread
- [ ] Squaring check with the ball joint fitted: ruler flat against the back and each side, the body should touch before a wheel (watch the front-left drive wheel)
- [ ] Stop the seed going over the top of the Mission 11 basket (for example, higher walls, a lip or a lid, or slow down the catch) and re-test — Jordan, Brynn, Jack
- [ ] Continue the forklift build — Ella, Amelia
- [ ] List the credible sources found for invasive species, with a link and one line on what each proves — Fedor, Alexis, Sylvie
