"""
GPS cradle walls.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
)

from Mount.GPSCradle.dimensions import (
    outer_width,
    outer_length,
)


def create_left(cfg):
    """
    Left wall.
    """

    wall = box(
        cfg.wall,
        outer_length(cfg),
        cfg.gps_height,
    )

    move(
        wall,
        0,
        0,
        cfg.wall,
    )

    return wall


def create_right(cfg):
    """
    Right wall.
    """

    wall = box(
        cfg.wall,
        outer_length(cfg),
        cfg.gps_height,
    )

    move(
        wall,
        outer_width(cfg) - cfg.wall,
        0,
        cfg.wall,
    )

    return wall


def create_front(cfg):
    """
    Front stop wall.
    """

    wall = box(
        outer_width(cfg),
        cfg.wall,
        cfg.gps_height,
    )

    move(
        wall,
        0,
        0,
        cfg.wall,
    )

    return wall