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
# Bridge
# --------------------------------------------------

def bridge_width(cfg):
    return (
        2 * outer_finger_width(cfg)
        + center_finger_width(cfg)
        + 2 * mount_clearance(cfg)
    )


def bridge_length(cfg):
    return cfg.wall


def bridge_thickness(cfg):
    return cfg.wall


# --------------------------------------------------
# Finger locations (local coordinates)
# --------------------------------------------------

def left_finger_x(cfg):
    return 0.0


def center_finger_x(cfg):
    return (
        outer_finger_width(cfg)
        + mount_clearance(cfg)
    )


def right_finger_x(cfg):
    return (
        outer_finger_width(cfg)
        + mount_clearance(cfg)
        + center_finger_width(cfg)
        + mount_clearance(cfg)
    )


# --------------------------------------------------
# Mount position
# --------------------------------------------------

def mount_x(cfg):
    return (
        outer_width(cfg)
        - bridge_width(cfg)
    ) / 2


def mount_y(cfg):
    return outer_length(cfg) - cfg.wall


def mount_z(cfg):
    return -cfg.wall