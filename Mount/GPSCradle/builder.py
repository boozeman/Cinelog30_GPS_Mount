"""
GPS Cradle Builder

Assembles the GPS cradle from the individual geometry modules.

This module contains no geometry itself.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    fuse_all,
)

from Mount.GPSCradle import (
    base,
    walls,
    rails,
    connector,
)


# --------------------------------------------------
# Assemble
# --------------------------------------------------

def assemble(cfg):
    """
    Assemble complete GPS cradle.
    """

    print("Assembling cradle")

    parts = []

    #
    # Base
    #

    parts.append(
        base.create(cfg)
    )

    #
    # Walls
    #

    parts.extend(
        walls.create(cfg)
    )

    #
    # Rails
    #

    parts.extend(
        rails.create(cfg)
    )

    print(f"Fusing {len(parts)} parts")

    shape = fuse_all(parts)

    #
    # Boolean operations
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