"""
GPS Cradle Builder

Main assembly for the GPS cradle.

This module contains no geometry itself.
Geometry is created in the dedicated modules:

    base.py
    walls.py
    connector.py
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    fuse_all,
    feature,
)

from Mount.GPSCradle import base
from Mount.GPSCradle import walls
from Mount.GPSCradle import connector


print("builder.py loaded")


# --------------------------------------------------
# Assemble
# --------------------------------------------------

def assemble(cfg):
    """
    Assemble complete GPS cradle.
    """

    print("Assembling cradle")

    parts = [

        base.create(cfg),

        walls.create_left(cfg),

        walls.create_right(cfg),

        walls.create_front(cfg),

    ]

    print(f"Fusing {len(parts)} parts")

    shape = fuse_all(parts)

    #
    # Boolean cuts
    #

    shape = connector.cut_connector(shape, cfg)
    shape = connector.cut_cable(shape, cfg)

    return shape


# --------------------------------------------------
# Builder
# --------------------------------------------------

def create(doc, parent, cfg):
    """
    Create GPS cradle feature.
    """

    print("Creating GPS cradle")

    shape = assemble(cfg)

    print(f"Valid : {shape.isValid()}")
    print(f"Volume: {shape.Volume:.2f}")

    return feature(
        doc,
        parent,
        "GPS_Cradle",
        shape,
    )