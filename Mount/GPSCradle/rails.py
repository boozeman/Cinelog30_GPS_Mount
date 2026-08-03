"""
GPS cradle slide rails.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
)

from Mount.GPSCradle.dimensions import (
    outer_width,
    rail_length,
    rail_y,
    rail_z,
)


# --------------------------------------------------
# Helpers
# --------------------------------------------------

def _rail(cfg):
    """
    Create one rectangular PCB rail.
    """

    return box(
        cfg.rail_width,
        rail_length(cfg),
        cfg.rail_height,
    )


# --------------------------------------------------
# Left rail
# --------------------------------------------------

def create_left(cfg):

    rail = _rail(cfg)

    x = cfg.wall
    print("LEFT rail x =", x)

    move(
        rail,
        x,
        rail_y(cfg),
        rail_z(cfg),
    )

    return rail


# --------------------------------------------------
# Right rail
# --------------------------------------------------

def create_right(cfg):

    rail = _rail(cfg)

    x = outer_width(cfg) - cfg.wall - cfg.rail_width
    print("RIGHT rail x =", x)
    
    move(
        rail,
        x,
        rail_y(cfg),
        rail_z(cfg),
    )

    return rail