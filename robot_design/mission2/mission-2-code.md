# Mission 2 Code (2026-10-06)

Code by **Jordan and Fedor**, written and test-run at the 2026-10-06 meeting. This is the SPIKE word-block project saved as [Mission_2_10-6-26.llsp3](Mission_2_10-6-26.llsp3) (open it in the SPIKE app). The project is named "301 code" inside the file and was last saved 2026-10-06 12:00 UTC (the hub is named "Dwayne"). This page is a plain-text reading of the blocks so the logic can be reviewed without the hub.

## Hardware assumed by the code

| Port | What the code uses it for |
|---|---|
| C | Left drive wheel (power is sent as a negative number, so it spins in reverse to go forward) |
| A | Right drive wheel (power sent as positive) |
| B | Attachment motor (raises and lowers the Mission 2 attachment) |
| Yaw | Hub gyro: the heading (turn angle) since the last `reset yaw` |

## The two My Blocks (the reusable PID code Jordan shared)

### Gyro Move (Distance, Speed)

Drives straight using the gyro to hold the heading, with an acceleration ramp.

```text
Start Power       = 15
Target Power      = Speed
End Power         = 20
Current Power     = Start Power
Slowdown Distance = Distance * 0.7        (start slowing at 70% of the trip)
TargetDistance    = Distance              (motor degrees, not mm)
Accel             = 5
Decel             = 8
KP                = 2.1
KI                = 2
Error_Sum         = 0
WaitTime          = 0.1 s

reset yaw
set motors C and A degree counters to 0
repeat until (|C position| + |A position|) / 2 > TargetDistance:
    if |C position| < Slowdown Distance:
        if Current Power < Target Power:  Current Power += Accel
    else:
        if Current Power > End Power:     Current Power -= Decel
    Error           = yaw
    Error_Sum       = Error_Sum + Error
    CorrectionValue = Error * KP + KI * (Error_Sum * WaitTime)
    motor C power   = -(Current Power - CorrectionValue)
    motor A power   = Current Power + CorrectionValue
    wait WaitTime
stop motors C and A
```

How it works:
- **P term:** `Error * KP`. Error is how many degrees the robot has turned from straight, so the correction grows with the error.
- **I term:** `KI * Error_Sum * WaitTime`. Error_Sum adds up the error every loop, so a small error that lasts gets a growing correction. `Error_Sum * WaitTime` is error x time, the standard integral. There is no D term.
- **Ramp:** starts at 15 power, speeds up by 5 each loop to the target (Speed), then after 70% of the distance slows by 8 each loop down to 20 so the stop is controlled. This is the acceleration ramp from the 2026-09-29 to-do list.
- **Distance** is measured as the average of both wheels' motor degrees, so one wheel slipping does not cut the run short.

### Gyro Turn (Degrees)

Turns to an angle using the gyro. Positive turns one way, negative the other.

```text
Min = 25, Max = 90
reset yaw
start: if Degrees > 0, motor C at -|Degrees| power; else motor A at |Degrees| power
repeat until |yaw| > |Degrees| - 3:
    Target Angle = |Degrees| - |yaw|       (angle still to go)
    limit Target Angle to between Min (25) and Max (90)
    motor power = Target Angle             (same motor as above)
stop motors C and A
```

How it works:
- **Speed is proportional to the angle left.** It starts fast and slows as the robot nears the target, but never below 25 power, so it doesn't stall, and never above 90.
- **Stops 3 degrees early** to allow for the robot coasting. This is a tuned value.
- **It is a pivot turn:** only one wheel drives (C for positive, A for negative) and the other stays still. See the turn definitions in the 2026-09-29 notes.

## Mission 2 main program

```text
when program starts
  set motor A speed 50
  motor B clockwise until |B power| > 65     (runs until the attachment hits its stop and the motor strains, then stops)
  Gyro Move 140, speed 90
  Gyro Turn 45
  Gyro Move 625, speed 90
  motor B speed 20, counterclockwise until |B power| > 65, then stop
  movement pair C and A: start moving back   (no stop block follows)
```

Notes for the team to check:
- The first block sets the speed of motor **A** (a drive wheel) to 50, but the next block starts motor **B**. If that was meant to set B's speed, it is the wrong port. **(confirm with Jordan and Fedor)**
- The last block backs away until the program ends. Confirm that is intended and the robot doesn't run into something.
- Two loose `Gyro Move 0, 90` blocks sit unattached in the workspace and do nothing. They can be deleted.

## Older drafts left in the project

Three unfinished scripts sit in the workspace next to the final My Blocks. They show how the code developed:

| Draft | What it does | Constants |
|---|---|---|
| Gyro drive, P only | Drives 1000 motor degrees straight, power 50 | KP 0.6 |
| Line follower | Follows a line edge using the colour sensor on port A (reflected light 50 is the target) | KP 0.6, Target Power 25 |
| Gyro drive with ramp | Gyro P control with a ramp using small Accel/Decel of 0.1 and no Slowdown tuning yet | Start 10, Target 80, End 10, KP not set in this script |

## What isn't recorded in the file

The file holds the final settings (KP 2.1, KI 2) but not the history of how they were chosen. That is in [kp-ki-tuning.md](kp-ki-tuning.md).
