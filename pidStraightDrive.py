#!/usr/bin/env pybricks-micropython

from pybricks.hubs import PrimeHub
from pybricks.motors import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait, StopWatch
import math

# ============================================================================
# SPIKE PRIME WHEEL CONFIGURATION
# ============================================================================
# Wheel diameter options for SPIKE Prime sets
WHEEL_DIAMETER_SMALL = 55    # Small wheel: 55mm
WHEEL_DIAMETER_LARGE = 84    # Large wheel: 84mm (approximately)

# Select which wheels your robot uses
WHEEL_DIAMETER = WHEEL_DIAMETER_LARGE  # Change to WHEEL_DIAMETER_SMALL if needed

# ============================================================================
# PID CONTROLLER CLASS FOR STRAIGHT-LINE DRIVING
# ============================================================================
class StraightDrivePID:
    """
    PID controller for driving a SPIKE Prime robot in a straight line.

    Uses gyro sensor to maintain heading and motor encoders for distance tracking.
    Implements acceleration and deceleration profiles.
    """

    def __init__(self, hub, left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER_LARGE):
        """
        Initialize the PID controller.

        Args:
            hub: PrimeHub instance
            left_motor: Left motor (Motor object)
            right_motor: Right motor (Motor object)
            wheel_diameter: Wheel diameter in mm
        """
        self.hub = hub
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.wheel_diameter = wheel_diameter
        self.wheel_circumference = math.pi * wheel_diameter

        # ====================================================================
        # PID PARAMETERS - TUNE THESE FOR YOUR ROBOT
        # ====================================================================
        # Heading correction (keeping straight)
        self.kp_heading = 2.0      # Proportional gain for heading
        self.ki_heading = 0.1      # Integral gain for heading
        self.kd_heading = 0.5      # Derivative gain for heading

        # Speed matching between motors (if one motor is faster)
        self.kp_speed = 1.2        # Proportional gain for speed matching

        # ====================================================================
        # ACCELERATION/DECELERATION PARAMETERS
        # ====================================================================
        self.max_acceleration = 100  # mm/s² - maximum acceleration
        self.max_deceleration = 150  # mm/s² - maximum deceleration

        # ====================================================================
        # DEBUGGING/MONITORING
        # ====================================================================
        self.debug_mode = False
        self.log_data = []

        # Reset controller state
        self.reset()

    def reset(self):
        """
        Reset controller state for a new drive sequence.

        Resets motor encoders, gyro heading, and PID state variables.
        Call this before each drive() sequence to ensure clean state.
        """
        # Reset motor positions and gyro
        self.left_motor.reset_angle()
        self.right_motor.reset_angle()
        self.hub.imu.reset_heading(0)

        # ====================================================================
        # PID STATE VARIABLES
        # ====================================================================
        self.previous_heading_error = 0
        self.heading_integral_error = 0
        self.previous_time = 0
        self.log_data = []

    def drive_straight(self, distance_mm, target_speed_mmps, stop_type=Stop.HOLD):
        """
        Drive the robot in a straight line with acceleration and deceleration.

        Args:
            distance_mm: Distance to drive in millimeters
            target_speed_mmps: Target speed in mm/s
            stop_type: How to stop (Stop.HOLD, Stop.COAST, Stop.BRAKE)
        """
        # Reset state for this drive sequence
        self.reset()

        # Initialize timers and tracking
        timer = StopWatch()
        start_left_angle = self.left_motor.angle()
        start_right_angle = self.right_motor.angle()

        # Calculate total time needed based on acceleration profile
        distance_accel = (target_speed_mmps ** 2) / (2 * self.max_acceleration)
        distance_decel = (target_speed_mmps ** 2) / (2 * self.max_deceleration)
        distance_constant = distance_mm - distance_accel - distance_decel

        if distance_constant < 0:
            # Distance too short for full acceleration/deceleration
            distance_accel = distance_mm / 3
            distance_decel = distance_mm / 3
            distance_constant = distance_mm - distance_accel - distance_decel

        time_accel = target_speed_mmps / self.max_acceleration
        time_constant = distance_constant / target_speed_mmps if distance_constant > 0 else 0
        time_decel = target_speed_mmps / self.max_deceleration
        total_time = time_accel + time_constant + time_decel

        if self.debug_mode:
            print(f"Drive Distance: {distance_mm}mm")
            print(f"Accel: {distance_accel:.1f}mm, Constant: {distance_constant:.1f}mm, Decel: {distance_decel:.1f}mm")
            print(f"Total Time: {total_time:.1f}s")

        self.previous_time = timer.time()

        while True:
            current_time = timer.time()
            dt = (current_time - self.previous_time) / 1000.0  # Convert to seconds
            self.previous_time = current_time

            if dt == 0:
                wait(1)
                continue

            # Calculate current distance traveled (average of both motors)
            left_distance = (self.left_motor.angle() - start_left_angle) * self.wheel_circumference / 360
            right_distance = (self.right_motor.angle() - start_right_angle) * self.wheel_circumference / 360
            current_distance = (left_distance + right_distance) / 2

            # Determine current phase and calculate desired speed
            if current_distance < distance_accel:
                # Acceleration phase: v = a * t (constant acceleration from rest)
                desired_speed = self.max_acceleration * (current_time / 1000)
                desired_speed = min(desired_speed, target_speed_mmps)
            elif current_distance < distance_accel + distance_constant:
                # Constant speed phase
                desired_speed = target_speed_mmps
            else:
                # Deceleration phase
                remaining_distance = distance_mm - current_distance
                desired_speed = math.sqrt(2 * self.max_deceleration * remaining_distance)
                desired_speed = max(0, desired_speed)

            # Calculate motor speeds using PID for heading correction
            heading = self.hub.imu.heading()
            heading_error = -heading  # Negative because gyro increases clockwise

            # PID calculation for heading
            self.heading_integral_error += heading_error * dt
            self.heading_integral_error = max(-100, min(100, self.heading_integral_error))  # Clamp integral

            heading_derivative = (heading_error - self.previous_heading_error) / dt if dt > 0 else 0
            self.previous_heading_error = heading_error

            heading_correction = (
                self.kp_heading * heading_error +
                self.ki_heading * self.heading_integral_error +
                self.kd_heading * heading_derivative
            )

            # Calculate individual motor speeds
            # Left motor gets positive correction, right motor gets negative
            left_speed = desired_speed + heading_correction
            right_speed = desired_speed - heading_correction

            # Convert mm/s to degrees per second
            left_speed_dps = (left_speed / self.wheel_circumference) * 360
            right_speed_dps = (right_speed / self.wheel_circumference) * 360

            # Apply speeds to motors
            self.left_motor.dc(left_speed_dps / 627 * 100)  # 627 dps = max speed, convert to %
            self.right_motor.dc(right_speed_dps / 627 * 100)

            # Log data for debugging
            if self.debug_mode and current_time % 100 == 0:
                self.log_data.append({
                    'time': current_time,
                    'distance': current_distance,
                    'heading': heading,
                    'left_speed': left_speed_dps,
                    'right_speed': right_speed_dps
                })

            # Check if we've reached the target distance
            if current_distance >= distance_mm:
                break

            wait(10)

        # Stop the motors
        self.left_motor.stop(stop_type)
        self.right_motor.stop(stop_type)

        if self.debug_mode:
            print(f"Drive Complete! Final distance: {current_distance:.1f}mm")

    def drive_to_point(self, x_mm, y_mm, speed_mmps):
        """
        Drive the robot to a specific coordinate using Pythagorean theorem.

        Args:
            x_mm: X coordinate in millimeters
            y_mm: Y coordinate in millimeters
            speed_mmps: Speed in mm/s
        """
        distance = math.sqrt(x_mm**2 + y_mm**2)
        angle_to_point = math.atan2(y_mm, x_mm) * 180 / math.pi

        # Rotate to face the point
        self.rotate_to_heading(angle_to_point)

        # Drive the distance
        self.drive_straight(distance, speed_mmps)

    def rotate_to_heading(self, target_heading):
        """
        Rotate the robot to face a specific heading using gyro.

        Args:
            target_heading: Target heading in degrees (0-359)
        """
        kp_rotate = 3.0
        max_rotation_speed = 150  # degrees per second

        while True:
            current_heading = self.hub.imu.heading()
            heading_error = target_heading - current_heading

            # Normalize angle to -180 to 180
            if heading_error > 180:
                heading_error -= 360
            elif heading_error < -180:
                heading_error += 360

            if abs(heading_error) < 2:
                break

            rotation_speed = max(-max_rotation_speed, min(max_rotation_speed, kp_rotate * heading_error))

            self.left_motor.dc(rotation_speed / 627 * 100)
            self.right_motor.dc(-rotation_speed / 627 * 100)

            wait(10)

        self.left_motor.stop(Stop.HOLD)
        self.right_motor.stop(Stop.HOLD)

    def calibrate_gyro(self):
        """Calibrate the IMU gyroscope. Robot must be stationary."""
        print("Calibrating gyro... Keep robot still!")
        self.hub.imu.reset_heading(0)
        wait(2000)
        print("Gyro calibration complete!")

    def tune_pid(self, kp=None, ki=None, kd=None):
        """Update PID parameters for tuning."""
        if kp is not None:
            self.kp_heading = kp
        if ki is not None:
            self.ki_heading = ki
        if kd is not None:
            self.kd_heading = kd


# ============================================================================
# EXAMPLE USAGE
# ============================================================================
if __name__ == "__main__":
    # Initialize hub and motors
    hub = PrimeHub()
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.B, Direction.CLOCKWISE)

    # Create PID controller
    drive = StraightDrivePID(hub, left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER_LARGE)
    drive.debug_mode = True

    # Beep to start
    hub.speaker.beep()

    try:
        # Calibrate gyro
        drive.calibrate_gyro()
        wait(1000)

        # Example 1: Drive straight 500mm at 200mm/s
        print("\n=== Drive Straight Test ===")
        drive.drive_straight(distance_mm=500, target_speed_mmps=200)
        wait(1000)

        # Example 2: Drive another 300mm
        print("\n=== Second Drive ===")
        drive.drive_straight(distance_mm=300, target_speed_mmps=150)
        wait(1000)

        # Example 3: Square pattern (optional)
        # Uncomment to test multiple straight drives
        # print("\n=== Square Pattern ===")
        # for i in range(4):
        #     drive.drive_straight(400, 150)
        #     drive.rotate_to_heading((i + 1) * 90)
        #     wait(500)

        print("\n=== All Tests Complete ===")
        hub.speaker.beep(1000, 100)

    except Exception as e:
        print(f"Error: {e}")
        left_motor.stop()
        right_motor.stop()
