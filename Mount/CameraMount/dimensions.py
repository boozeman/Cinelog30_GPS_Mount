"""
Shared dimensions for the camera mount.
"""

from __future__ import annotations

from Mount.GPSCradle.dimensions import (
    outer_width,
    outer_length,
)


# --------------------------------------------------
# Bridge
# --------------------------------------------------

def bridge_length(cfg):
    """
    Bridge length (Y).
    """

    return cfg.bridge_length


def bridge_thickness(cfg):
    """
    Bridge thickness (Z).
    """

    return cfg.bridge_thickness


# --------------------------------------------------
# Fingers
# --------------------------------------------------

def outer_finger_width(cfg):
    return cfg.outer_finger_width


def center_finger_width(cfg):
    return cfg.center_finger_width


def finger_height(cfg):
    return cfg.finger_height


def finger_gap(cfg):
    return cfg.finger_gap


def finger_hole_diameter(cfg):
    return cfg.finger_hole_diameter


def finger_hole_from_tip(cfg):
    return cfg.finger_hole_from_tip


# --------------------------------------------------
# Overall dimensions
# --------------------------------------------------

def mount_width(cfg):
    """
    Total width of the three-finger mount.
    """

    return (
        2 * outer_finger_width(cfg)
        + center_finger_width(cfg)
    )


def bridge_width(cfg):

    return (
        2 * outer_finger_width(cfg)
        + center_finger_width(cfg)
        + 2 * cfg.mount_clearance
    )

def slot_width(cfg):
    return cfg.mount_clearance

# --------------------------------------------------
# Position
# --------------------------------------------------

def mount_x(cfg):
    """
    Center the mount under the cradle.
    """

    return (
        outer_width(cfg)
        - bridge_width(cfg)
    ) / 2


def mount_y(cfg):
    """
    Bridge overlaps the cradle back wall.
    """

    return (
        outer_length(cfg)
        - bridge_length(cfg)
    )


def mount_z(cfg):
    """
    Attach bridge to the bottom of the cradle.
    """

    return -bridge_thickness(cfg)