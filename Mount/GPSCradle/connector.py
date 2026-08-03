"""
Connector openings for the GPS cradle.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
    cut,
)

from Mount.GPSCradle.dimensions import (
    connector_x,
    connector_y,
)


# --------------------------------------------------
# Connector opening
# --------------------------------------------------

def cut_connector(shape, cfg):
    """
    Cut opening for the SH connector.
    """

    opening = box(
        cfg.connector_width,
        cfg.connector_depth,
        cfg.connector_height,
    )

    move(
        opening,
        connector_x(cfg),
        connector_y(cfg),
        cfg.wall,
    )

    return cut(shape, opening)


# --------------------------------------------------
# Cable opening
# --------------------------------------------------

def cut_cable(shape, cfg):
    """
    Cut cable exit slot in the floor.
    """

    slot = box(
        cfg.cable_hole_width,
        cfg.connector_depth + 1.0,
        cfg.wall + 0.5,
    )

    move(
        slot,
        connector_x(cfg),
        connector_y(cfg),
        -0.25,
    )

    return cut(shape, slot)