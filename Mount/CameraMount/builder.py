"""
Support Arm Builder

Assembles the support arm.
"""

from __future__ import annotations

from body import add_feature

from Mount.Utils.geometry import (
    move,
)

from Mount.CameraMount import base

from Mount.CameraMount.dimensions import (
    arm_x,
    arm_y,
    arm_z,
)


# --------------------------------------------------
# Assemble
# --------------------------------------------------

def assemble(cfg):
    """
    Assemble the support arm.
    """

    shape = base.create(cfg)

    move(
        shape,
        arm_x(cfg),
        arm_y(cfg),
        arm_z(cfg),
    )

    return shape


# --------------------------------------------------
# Builder
# --------------------------------------------------

def create(doc, parent, cfg):
    """
    Create the support arm.
    """

    print("Creating support arm")

    shape = assemble(cfg)

    return add_feature(
        doc,
        parent,
        "Support_Arm",
        shape,
    )