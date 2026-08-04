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

# Finger locations are relative to the origin at the center of the mount width, and at the front of the mount (the end of the fingers).

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

# Overall mount width is the distance between the two outer fingers.
def mount_width(cfg):
    return (
        2 * outer_finger_width(cfg)
        + center_finger_width(cfg)
        + 2 * (cfg.ear_gap + mount_clearance(cfg))
    )

# --------------------------------------------------
# Mount position
# --------------------------------------------------

# Mount is centered under the cradle.
def mount_x(cfg):

    return (
        outer_width(cfg)
        - mount_width(cfg)
    ) / 2

# Mount is positioned at the back of the cradle.
def mount_y(cfg):
    return (
        outer_length(cfg)
        - finger_length(cfg)
    ) / 2

# Mount is positioned at the bottom of the cradle.
def mount_z(cfg):
    return -cfg.wall


# --------------------------------------------------
# Hole position
# --------------------------------------------------

# Hole is at the center of the mount width.
def hole_x(cfg):
    return 0.0

# Finger hole is at the center of the finger length.
def hole_y(cfg):
    return finger_length(cfg) / 2

# Finger hole is at the center of the finger height.
def hole_z(cfg):
    return -finger_height(cfg) / 2

# hole_length is the overall width of the mount, which is the distance between the two outer fingers.
def hole_length(cfg):
    return mount_width(cfg)