"""
GPS cradle base.

Creates the bottom plate of the GPS cradle.
"""

from __future__ import annotations

from Mount.Utils.geometry import box
from Mount.GPSCradle.dimensions import (
    outer_width,
    outer_length,
)


def create(cfg):
    """
    Create cradle base plate.
    """

    return box(
        outer_width(cfg),
        outer_length(cfg),
        cfg.wall,
    )