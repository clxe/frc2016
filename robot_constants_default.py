#!/usr/bin/env python3

# JOYSTICK
#===============================================================================

JOYSTICK_INDEX = 0 # Joystick port index
FORWARD_AXIS_INDEX = 1 # Forward/back joystick axis index
TURN_AXIS_INDEX = 3 # Left/right joystick axis index
TURBO_BUTTON_INDEX = 2 # Turbo button index

# MOTORS
#===============================================================================

L_MOTOR_INDICES = [1, 3] # Left motor CAN port index
R_MOTOR_INDICES = [2, 4] # Right motor CAN port index
MOTOR_DEADBAND = 0.04 # Deadband of the wheel motors

# MOVEMENT
#===============================================================================

FORWARD_DIVISOR = 4 # Forward/back movement speed divisor
PIVOT_DIVISOR = 6 # Stationary pivot speed divisor
ALLOW_TURBO = True
TURBO_MULT = 2 # Turbo speed multiplier
