"""
Support arm base.

Creates the rectangular arm body.
"""

from __future__ import annotations

from Mount.Utils.geometry import box

from Mount.Arm.dimensions import (
    arm_width,
    arm_height,
    arm_thickness,
)


def create(cfg):
    """
    Create the support arm body.
    """

    return box(
        arm_width(cfg),
        arm_thickness(cfg),
        arm_height(cfg),
    )