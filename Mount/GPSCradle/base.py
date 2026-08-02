"""
GPS cradle base.

Creates the bottom plate of the cradle.
"""

from __future__ import annotations

from Mount.Utils.geometry import box


def create(cfg):
    """
    Create cradle base plate.
    """

    outer_width = cfg.gps_width + 2 * cfg.wall
    outer_length = cfg.gps_length + 2 * cfg.wall

    return box(
        outer_width,
        outer_length,
        cfg.wall,
    )