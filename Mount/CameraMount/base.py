"""
Support arm base.

Creates the rectangular support arm body.
"""

from __future__ import annotations

from Mount.Utils.geometry import box

from Mount.CameraMount.dimensions import (
    arm_width,
    arm_length,
    arm_thickness,
    
)


def create(cfg):
    """
    Create the support arm body.

    The arm is created at the origin. Positioning is handled
    by the builder.
    """

    return box(
        arm_width(cfg),
        arm_length(cfg),
        arm_thickness(cfg),
    )