"""
Slide rail generator.

The rails are integrated into the side walls.
Only the retaining lip extends inside the cradle.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
)


def create_left(cfg):
    """
    Left retaining lip.
    """

    rail = box(
        cfg.rail_lip_width,
        cfg.rail_length,
        cfg.rail_lip_thickness,
    )

    move(
        rail,
        cfg.wall,
        cfg.wall + cfg.rail_entry,
        cfg.wall + cfg.gps_height - cfg.pcb_thickness,
    )

    return rail


def create_right(cfg):
    """
    Right retaining lip.
    """

    rail = box(
        cfg.rail_lip_width,
        cfg.rail_length,
        cfg.rail_lip_thickness,
    )

    move(
        rail,
        cfg.wall + cfg.gps_width - cfg.rail_lip_width,
        cfg.wall + cfg.rail_entry,
        cfg.wall + cfg.gps_height - cfg.pcb_thickness,
    )

    return rail