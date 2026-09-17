#!/usr/bin/env pybricks-micropython

"""
Example programs using the PID straight-line drive controller.
Uncomment the example you want to run.
"""

from pybricks.hubs import PrimeHub
from pybricks.motors import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait
from pidStraightDrive import StraightDrivePID, WHEEL_DIAMETER_LARGE, WHEEL_DIAMETER_SMALL

# Initialize hub and motors
hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

# Create PID controller (using large wheels)
drive = StraightDrivePID(hub, left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER_LARGE)
drive.debug_mode = True


# ============================================================================
# EXAMPLE 1: Simple Straight Drive
# ============================================================================
def example_simple_drive():
    """Drive 500mm forward at 200mm/s."""
    print("\n=== Example 1: Simple Straight Drive ===")
    hub.speaker.beep()

    drive.calibrate_gyro()
    wait(1000)

    drive.drive_straight(distance_mm=500, target_speed_mmps=200)

    hub.speaker.beep(1000, 100)
    print("Complete!")


# ============================================================================
# EXAMPLE 2: Multiple Segments
# ============================================================================
def example_multiple_segments():
    """Drive forward in three segments with different speeds."""
    print("\n=== Example 2: Multiple Segments ===")
    hub.speaker.beep()

    drive.calibrate_gyro()
    wait(1000)

    segments = [
        {"distance": 300, "speed": 100},
        {"distance": 500, "speed": 200},
        {"distance": 400, "speed": 150},
    ]

    for i, segment in enumerate(segments):
        print(f"\nSegment {i+1}: {segment['distance']}mm at {segment['speed']}mm/s")
        drive.drive_straight(
            distance_mm=segment["distance"],
            target_speed_mmps=segment["speed"]
        )
        wait(1000)

    hub.speaker.beep(1000, 100)
    print("Complete!")


# ============================================================================
# EXAMPLE 3: Square Pattern
# ============================================================================
def example_square_pattern():
    """Drive in a square pattern (4 sides of 400mm each)."""
    print("\n=== Example 3: Square Pattern ===")
    hub.speaker.beep()

    drive.calibrate_gyro()
    wait(1000)

    side_length = 400  # mm
    speed = 150  # mm/s

    for i in range(4):
        print(f"\nSide {i+1}: Driving {side_length}mm")
        drive.drive_straight(distance_mm=side_length, target_speed_mmps=speed)

        # Rotate 90 degrees
        next_heading = (i + 1) * 90
        print(f"Rotating to {next_heading}°")
        drive.rotate_to_heading(next_heading)

        wait(500)

    hub.speaker.beep(1000, 100)
    print("Complete!")


# ============================================================================
# EXAMPLE 4: Triangle Pattern
# ============================================================================
def example_triangle_pattern():
    """Drive in an equilateral triangle pattern."""
    print("\n=== Example 4: Triangle Pattern ===")
    hub.speaker.beep()

    drive.calibrate_gyro()
    wait(1000)

    side_length = 500  # mm
    speed = 150  # mm/s
    angle = 120  # 120° turn for equilateral triangle

    for i in range(3):
        print(f"\nSide {i+1}: Driving {side_length}mm")
        drive.drive_straight(distance_mm=side_length, target_speed_mmps=speed)

        # Rotate 120 degrees
        next_heading = (i + 1) * angle
        if next_heading >= 360:
            next_heading -= 360
        print(f"Rotating to {next_heading}°")
        drive.rotate_to_heading(next_heading)

        wait(500)

    hub.speaker.beep(1000, 100)
    print("Complete!")


# ============================================================================
# EXAMPLE 5: Long Distance Drive (Endurance Test)
# ============================================================================
def example_long_distance():
    """Drive 3 meters at constant speed to test stability over distance."""
    print("\n=== Example 5: Long Distance Drive ===")
    hub.speaker.beep()

    drive.calibrate_gyro()
    wait(1000)

    distance = 3000  # 3 meters
    speed = 200  # mm/s

    print(f"Driving {distance/1000}m at {speed}mm/s")
    drive.drive_straight(distance_mm=distance, target_speed_mmps=speed)

    hub.speaker.beep(1000, 100)
    print("Complete!")


# ============================================================================
# EXAMPLE 6: Point Navigation (XY Coordinates)
# ============================================================================
def example_point_navigation():
    """Navigate to specific coordinates using XY positioning."""
    print("\n=== Example 6: Point Navigation ===")
    hub.speaker.beep()

    drive.calibrate_gyro()
    wait(1000)

    # Drive to (400mm right, 300mm forward)
    print("\nDriving to point (400, 300)")
    drive.drive_to_point(x_mm=400, y_mm=300, speed_mmps=150)

    wait(500)

    # Return to origin (going backward and left)
    print("Returning to origin (0, 0)")
    drive.drive_to_point(x_mm=-400, y_mm=-300, speed_mmps=150)

    hub.speaker.beep(1000, 100)
    print("Complete!")


# ============================================================================
# EXAMPLE 7: Speed Variation Test
# ============================================================================
def example_speed_variation():
    """Test drive at different speeds to find optimal range."""
    print("\n=== Example 7: Speed Variation Test ===")
    hub.speaker.beep()

    drive.calibrate_gyro()
    wait(1000)

    speeds = [50, 100, 150, 200, 250]
    distance = 400  # mm

    for speed in speeds:
        print(f"\nDriving at {speed}mm/s")
        drive.drive_straight(distance_mm=distance, target_speed_mmps=speed)
        wait(1000)

    hub.speaker.beep(1000, 100)
    print("Complete!")


# ============================================================================
# EXAMPLE 8: PID Tuning Test
# ============================================================================
def example_pid_tuning():
    """Test different PID values and compare results."""
    print("\n=== Example 8: PID Tuning Test ===")
    hub.speaker.beep()

    drive.calibrate_gyro()
    wait(1000)

    tuning_sets = [
        {"name": "Conservative", "kp": 1.5, "ki": 0.05, "kd": 0.3},
        {"name": "Balanced", "kp": 2.0, "ki": 0.1, "kd": 0.5},
        {"name": "Aggressive", "kp": 3.0, "ki": 0.15, "kd": 0.8},
    ]

    for tuning in tuning_sets:
        print(f"\n--- Testing {tuning['name']} ---")
        drive.tune_pid(kp=tuning["kp"], ki=tuning["ki"], kd=tuning["kd"])
        print(f"Kp={tuning['kp']}, Ki={tuning['ki']}, Kd={tuning['kd']}")

        drive.calibrate_gyro()
        wait(500)

        drive.drive_straight(distance_mm=1000, target_speed_mmps=200)
        wait(1500)

    hub.speaker.beep(1000, 100)
    print("Complete!")


# ============================================================================
# MAIN - Select which example to run
# ============================================================================
if __name__ == "__main__":
    try:
        # Uncomment the example you want to run:

        # example_simple_drive()
        # example_multiple_segments()
        example_square_pattern()
        # example_triangle_pattern()
        # example_long_distance()
        # example_point_navigation()
        # example_speed_variation()
        # example_pid_tuning()

    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        left_motor.stop()
        right_motor.stop()
