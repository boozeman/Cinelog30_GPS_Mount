"""
Camera mount base.

Creates the bridge and finger blank.

The three mounting fingers will be cut from the
finger blank in later steps.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
    fuse,
)

from Mount.CameraMount.dimensions import (
    mount_width,
    bridge_length,
    bridge_thickness,
    finger_height,
    outer_finger_width,
    center_finger_width,
    finger_gap,
)


# --------------------------------------------------
# Camera mount
# --------------------------------------------------

def create(cfg):
    """
    Create the camera mount blank.
    """

    #
    # Bridge
    #

    bridge = box(
        mount_width(cfg),
        bridge_length(cfg),
        bridge_thickness(cfg),
    )

    #
    # Finger blank
    #

    fingers = box(
        mount_width(cfg),
        bridge_thickness(cfg),
        finger_height(cfg),
    )

    #
    # Attach fingers to bridge.
    #
    # The bridge sits against the cradle bottom.
    # The fingers extend downward.
    #

    move(
        fingers,
        0,
        bridge_length(cfg),
        bridge_thickness(cfg) - finger_height(cfg),
    )

    return fuse(
        bridge,
        fingers,
    )