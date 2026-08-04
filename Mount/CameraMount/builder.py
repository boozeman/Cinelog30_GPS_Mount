"""
Camera Mount Builder

Assembles the camera mount.
"""

from __future__ import annotations

from body import add_feature

from Mount.Utils.geometry import move

from Mount.CameraMount import base

from Mount.CameraMount.dimensions import (
    mount_x,
    mount_y,
    mount_z,
)

from Mount.Utils.geometry import (
    box,
    move,
    fuse,
    cut,
)

# --------------------------------------------------
# Assemble
# --------------------------------------------------

def assemble(cfg):
    """
    Assemble the camera mount.
    """

    shape = base.create(cfg)

    move(
        shape,
        mount_x(cfg),
        mount_y(cfg),
        mount_z(cfg),
    )

    return shape


# --------------------------------------------------
# Builder
# --------------------------------------------------

def create(doc, parent, cfg):
    """
    Create the camera mount.
    """

    print("Creating camera mount")

    shape = assemble(cfg)

    return add_feature(
        doc,
        parent,
        "Camera_Mount",
        shape,
    )