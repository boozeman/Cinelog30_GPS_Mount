"""
Shared dimensions for the camera mount.
"""

from __future__ import annotations

from Mount.GPSCradle.dimensions import (
    outer_width,
    outer_length,
)


# --------------------------------------------------
# Finger dimensions
# --------------------------------------------------

def finger_height(cfg):
    return cfg.finger_height

def finger_length(cfg):
    return cfg.finger_length

def outer_finger_width(cfg):
    return cfg.outer_finger_width

def center_finger_width(cfg):
    return cfg.center_finger_width

def mount_clearance(cfg):
    return cfg.mount_clearance

def finger_hole_diameter(cfg):
    return cfg.finger_hole_diameter

def finger_hole_from_tip(cfg):
    return cfg.finger_hole_from_tip


# --------------------------------------------------
# Finger locations (local coordinates)
# --------------------------------------------------

def left_finger_x(cfg):
    return 0.0


def center_finger_x(cfg):
    return (
        outer_finger_width(cfg)
        + cfg.ear_gap
        + mount_clearance(cfg)
    )


def right_finger_x(cfg):
    return (
        outer_finger_width(cfg)
        + cfg.ear_gap
        + mount_clearance(cfg)
        + center_finger_width(cfg)
        + cfg.ear_gap
        + mount_clearance(cfg)
    )

# --------------------------------------------------
# Overall mount width
# --------------------------------------------------

def mount_width(cfg):
    return (
        2 * outer_finger_width(cfg)
        + center_finger_width(cfg)
        + 2 * (cfg.ear_gap + mount_clearance(cfg))
    )

# --------------------------------------------------
# Mount position
# --------------------------------------------------

def mount_x(cfg):
    """
    Center the camera mount under the cradle.
    """
    return (
        outer_width(cfg)
        - mount_width(cfg)
    ) / 2

def mount_y(cfg):
    return (
        outer_length(cfg)
        - finger_length(cfg)
    ) / 2

def mount_z(cfg):
    return -cfg.wall


# --------------------------------------------------
# Hole position
# --------------------------------------------------

def hole_x(cfg):
    return center_finger_x(cfg)

def hole_y(cfg):
    """
    Hole center measured from the finger root.
    """
    return finger_hole_from_tip(cfg)


def hole_z(cfg):
    """
    Hole passes through the finger center.
    """
    return -finger_height(cfg)

def hole_length(cfg):
    return mount_width(cfg)