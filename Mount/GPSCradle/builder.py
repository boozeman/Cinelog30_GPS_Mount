"""
GPS Cradle Builder

Main assembly module.

This module contains no geometry.
Geometry is delegated to the dedicated modules.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    fuse_all,
    feature,
    check,
)

from Mount.GPSCradle import base
from Mount.GPSCradle import walls
from Mount.GPSCradle import connector
from Mount.GPSCradle import rails


# --------------------------------------------------
# Assembly
# --------------------------------------------------

def assemble(cfg):
    """
    Assemble the complete GPS cradle.
    """

    print("Assembling GPS cradle")

    parts = [

        base.create(cfg),

        walls.create_left(cfg),

        walls.create_right(cfg),

        walls.create_front(cfg),

        rails.create_left(cfg),
        
        rails.create_right(cfg),
    ]

    print(f"Fusing {len(parts)} parts")

    shape = fuse_all(parts)

    #
    # Boolean operations
    #

    shape = connector.cut_connector(shape, cfg)
    shape = connector.cut_cable(shape, cfg)

    check(shape, "GPS Cradle")

    return shape


# --------------------------------------------------
# Public API
# --------------------------------------------------

def create(doc, parent, cfg):
    """
    Create the GPS cradle feature.
    """

    print("Creating GPS cradle")

    shape = assemble(cfg)

    return feature(
        doc,
        parent,
        "GPS_Cradle",
        shape,
    )