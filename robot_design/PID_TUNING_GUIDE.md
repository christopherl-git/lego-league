# PID Straight-Line Driving Tuning Guide

## Overview

The `pidStraightDrive.py` module implements a PID controller for driving SPIKE Prime robots in a straight line while maintaining heading (direction) using the built-in gyroscope sensor.

## Hardware Configuration

### Motors
- **Left Motor**: Port A (should rotate counterclockwise when moving forward)
- **Right Motor**: Port B (should rotate clockwise when moving forward)

### Wheel Sizes
Choose your wheel diameter based on your SPIKE Prime set:

```python
# Small wheels (55mm diameter)
WHEEL_DIAMETER = WHEEL_DIAMETER_SMALL  # 55mm

# Large wheels (84mm diameter) - Default
WHEEL_DIAMETER = WHEEL_DIAMETER_LARGE  # 84mm
```

## Understanding PID Parameters

### Heading Correction (Gyro-based)

The robot uses three PID gains to maintain a straight line:

```python
self.kp_heading = 2.0    # Proportional gain
self.ki_heading = 0.1    # Integral gain
self.kd_heading = 0.5    # Derivative gain
```

#### `kp_heading` (Proportional)
- **Effect**: Direct response to heading error
- **Too Low**: Robot drifts; slow correction
- **Too High**: Robot oscillates side-to-side
- **Tuning**: Start at 2.0, increase gradually if drifting, decrease if oscillating

#### `ki_heading` (Integral)
- **Effect**: Eliminates steady-state drift
- **Too Low**: Persistent drift over long distances
- **Too High**: Slow response; overshooting
- **Tuning**: Start at 0.1, increase if drift accumulates over time

#### `kd_heading` (Derivative)
- **Effect**: Dampens oscillations; improves stability
- **Too Low**: Robot overshoots corrections
- **Too High**: Sluggish, unresponsive
- **Tuning**: Start at 0.5, adjust if oscillation is too pronounced

### Acceleration/Deceleration

```python
self.max_acceleration = 100  # mm/s²
self.max_deceleration = 150  # mm/s²
```

- **Acceleration**: How quickly the robot speeds up (smoother = lower value)
- **Deceleration**: How quickly the robot slows down (should be higher than acceleration)

## Tuning Procedure

### Step 1: Basic Setup
1. Place robot on level ground away from obstacles
2. Ensure wheels are properly aligned
3. Set `debug_mode = True` to see real-time data

### Step 2: Test Short Distances
```python
drive.drive_straight(distance_mm=300, target_speed_mmps=100)
```

Start with short distances and low speeds to identify issues.

### Step 3: Proportional Tuning (Kp)
1. Set `ki_heading = 0.0` and `kd_heading = 0.0`
2. Test with Kp values: 1.0, 2.0, 3.0, 4.0
3. Choose the value that drives most straight without oscillation
4. **Note**: Some oscillation is expected; it means Kp is strong enough

### Step 4: Derivative Tuning (Kd)
1. Keep best Kp value
2. Set `ki_heading = 0.0`
3. Increase Kd from 0.1 to 1.0 to dampen oscillation
4. Find balance between oscillation and responsiveness

### Step 5: Integral Tuning (Ki)
1. Keep tuned Kp and Kd values
2. Increase Ki from 0.05 to 0.3
3. Drive longer distances (1-2 meters) to test drift elimination
4. Use smallest Ki that still eliminates drift

### Step 6: Long Distance Testing
```python
drive.drive_straight(distance_mm=2000, target_speed_mmps=200)
```

Test with longer distances and higher speeds to ensure stability.

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Robot drifts left/right | Low Kp or Ki | Increase Kp or Ki |
| Oscillates side-to-side | High Kp or low Kd | Decrease Kp, increase Kd |
| Overshoots corrections | High Kd | Decrease Kd |
| Drifts after long distance | Low Ki | Increase Ki (also check wheel alignment) |
| Erratic behavior | Motor directions wrong | Check motor Direction settings |
| Slow response | Low Kp | Increase Kp gradually |

## Example Tuning Values

### Conservative (Slow, Very Stable)
```python
kp_heading = 1.5
ki_heading = 0.05
kd_heading = 0.3
max_acceleration = 50
max_deceleration = 75
```

### Balanced (Default)
```python
kp_heading = 2.0
ki_heading = 0.1
kd_heading = 0.5
max_acceleration = 100
max_deceleration = 150
```

### Aggressive (Fast, Requires Tuning)
```python
kp_heading = 3.0
ki_heading = 0.15
kd_heading = 0.8
max_acceleration = 150
max_deceleration = 200
```

## Usage Examples

### Simple Straight Drive
```python
hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

drive = StraightDrivePID(hub, left_motor, right_motor)
drive.calibrate_gyro()
drive.drive_straight(distance_mm=500, target_speed_mmps=200)
```

### Driving to a Point (XY Coordinates)
```python
# Drive 300mm forward and 200mm to the right
drive.drive_to_point(x_mm=200, y_mm=300, speed_mmps=150)
```

### Rotating to a Heading
```python
# Rotate to face 90 degrees (right)
drive.rotate_to_heading(90)

# Drive forward
drive.drive_straight(distance_mm=400, target_speed_mmps=200)
```

### Square Pattern
```python
for i in range(4):
    drive.drive_straight(400, 200)
    drive.rotate_to_heading((i + 1) * 90)
    wait(500)
```

## Debugging Features

### Enable Debug Mode
```python
drive.debug_mode = True
```

This will print:
- Total drive distance and time estimates
- Current heading error
- Motor speeds during drive

### Inspect Logged Data
```python
drive.drive_straight(500, 200)

# Print data points
for point in drive.log_data:
    print(f"Time: {point['time']}ms, Distance: {point['distance']:.1f}mm, "
          f"Heading: {point['heading']}°")
```

## Performance Tips

1. **Motor Alignment**: Ensure wheels are perpendicular to the robot's direction of motion
2. **Floor Surface**: Use consistent, smooth surfaces for best results
3. **Wheel Condition**: Check for debris on wheels; clean before driving
4. **Speed Range**: Best results between 100-250 mm/s for typical tuning
5. **Gyro Calibration**: Always calibrate before starting new driving sequence
6. **Battery Level**: Low battery can affect motor responsiveness; maintain good charge

## Technical Details

### Coordinate System
- **X-axis**: Right (positive), Left (negative)
- **Y-axis**: Forward (positive), Backward (negative)
- **Heading**: 0° = Forward, 90° = Right, 180° = Backward, 270° = Left

### Velocity Calculation
- Wheel circumference = π × diameter (mm)
- Motor speed in mm/s → degrees/second: (speed / circumference) × 360
- Max motor speed (SPIKE Prime): ~627 dps

### PID Error Correction
```
correction = Kp × error + Ki × Σerror × dt + Kd × (derror/dt)
```

Where:
- `error` = target heading - current heading
- `Σerror` = sum of all errors over time
- `derror/dt` = rate of change of error
