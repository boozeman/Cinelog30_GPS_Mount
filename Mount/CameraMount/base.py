"""
Camera mount base.

Creates the bridge and three mounting fingers.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
    fuse_all,
)

from Mount.CameraMount.dimensions import (
    finger_height,
    finger_length,
    outer_finger_width,
    center_finger_width,
    left_finger_x,
    center_finger_x,
    right_finger_x,
)


def create(cfg):
    """
    Create camera mount geometry.

    Geometry is created at the origin.
    """

    parts = []

    #
    # Common finger position
    #

    finger_y = 0.0

    finger_z = -finger_height(cfg)

    #
    # Left finger
    #

    finger = box(
        outer_finger_width(cfg),       
        finger_length(cfg),
        finger_height(cfg),
    )

    move(
        finger,
        left_finger_x(cfg),
        finger_y,
        finger_z,
    )

    parts.append(finger)

    #
    # Center finger
    #

    finger = box(
        center_finger_width(cfg),       
        finger_length(cfg),
        finger_height(cfg),
    )

    move(
        finger,
        center_finger_x(cfg),
        finger_y,
        finger_z,
    )

    parts.append(finger)

    #
    # Right finger
    #

    finger = box(
        outer_finger_width(cfg),        
        finger_length(cfg),
        finger_height(cfg),
        
        
    )

    move(
        finger,
        right_finger_x(cfg),
        finger_y,
        finger_z,
    )

    parts.append(finger)

    return fuse_all(parts)