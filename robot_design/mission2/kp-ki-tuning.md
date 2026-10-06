# How Jordan Tuned Kp and Ki

Judges ask how a team chose its numbers, so this page records the tuning. It has two parts: what the project file proves, and the questions to ask Jordan to fill in the rest. Anything marked **(confirm)** has to come from Jordan, because the file stores only the final settings.

## What the file shows

- **Final values in `Gyro Move`:** **Kp = 2.1** and **Ki = 2**. There is no Kd (derivative) term.
- **The loop runs every 0.1 s** (`WaitTime`). The integral is computed as `Ki x Error_Sum x WaitTime`, so Ki is in correction power per degree-second.
- **The earlier drafts used Kp = 0.6** (the P-only gyro drive and the line follower, both left in the workspace). So Kp was probably raised from 0.6 to 2.1, with Ki added after the P-only version. **(confirm)**
- **Starting point in the repo:** our [PID_TUNING_GUIDE.md](../PID_TUNING_GUIDE.md) suggests Kp 2.0, Ki 0.1, Kd 0.5 for the Python version. Jordan's Kp 2.1 is close to that, but Ki 2 is 20 times larger. The two are in different code and units (the block version multiplies by the 0.1 s loop time), so they are not directly comparable. **(confirm whether Jordan used the guide)**
- **Other values tuned alongside:** ramp Accel 5, Decel 8, slowdown at 70% of the distance, start power 15, end power 20. For turns: min power 25, max 90, stop 3 degrees early.

## What to record (ask Jordan)

Fill in a row for each change. The actual numbers and results are what a judge wants to see.

| Step | Kp | Ki | What the robot did | What Jordan changed next and why |
|---|---|---|---|---|
| 1. Start | 0.6 **(confirm)** | 0 | **(confirm)** | |
| 2. | **(confirm)** | | | |
| 3. | | | | |
| Final | 2.1 | 2 | **(confirm)** | Settled on these values |

Questions:
1. **What test did you use?** (for example, drive a set distance and measure how far off straight the robot ended up, and how many repeats)
2. **What did Kp too low look like, and Kp too high?** Does the robot drift, or wobble side to side?
3. **Why add Ki?** What was Kp alone not fixing? (for example, a steady drift that stayed after the P correction)
4. **Did Ki ever cause trouble?** Ki can build up (called windup) and make the robot swing past straight. Error_Sum is not capped in this code and resets at the start of each Gyro Move.
5. **Did the test runs at the 2026-10-06 meeting change anything?** What were the results on Mission 2?
6. **Did the wheels or the ball caster change how it needed to be tuned?**

## Rules of thumb behind the tuning

These match what the 2026-09-29 PID session taught and what our tuning guide says:
- **Raise Kp** until the robot corrects well, and back off when it starts to wobble.
- **Add a little Ki** only if it still ends a bit off straight or drifts the same way every time.
- Change **one number at a time** and repeat the same test, so you know which change caused the result.

## Where to keep results

When the tuning is confirmed, add the final test (the same distance run 10 times, and the spread in where the robot ends up) to the robot design log as proof that the numbers work.
