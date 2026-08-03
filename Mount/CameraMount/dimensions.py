"""
Shared dimensions for the support arm.
"""

from __future__ import annotations

from Mount.GPSCradle.dimensions import (
    outer_width,
    outer_length,
)


# --------------------------------------------------
# Arm size
# --------------------------------------------------

# --------------------------------------------------
# Arm size
# --------------------------------------------------

def arm_width(cfg):
    return cfg.arm_width


def arm_length(cfg):
    return cfg.arm_length


def arm_thickness(cfg):
    return cfg.arm_thickness


def arm_angle(cfg):
    return cfg.arm_angle_deg

# --------------------------------------------------
# Arm position
# --------------------------------------------------

def arm_x(cfg):
    """
    Arm starts at the left side of the cradle.
    """

    return (outer_width(cfg) - arm_width(cfg)) / 2


def arm_y(cfg):
    return outer_length(cfg)


def arm_z(cfg):
    """
    Arm starts from the cradle floor.
    """
    return -arm_thickness(cfg)

    

