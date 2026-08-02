"""
GPS cradle walls.

Creates the left, right and front walls.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
)


def create_left(cfg):
    """
    Left side wall.
    """

    outer_length = cfg.gps_length + 2 * cfg.wall

    wall = box(
        cfg.wall,
        outer_length,
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
    Right side wall.
    """

    outer_width = cfg.gps_width + 2 * cfg.wall
    outer_length = cfg.gps_length + 2 * cfg.wall

    wall = box(
        cfg.wall,
        outer_length,
        cfg.gps_height,
    )

    move(
        wall,
        outer_width - cfg.wall,
        0,
        cfg.wall,
    )

    return wall


def create_front(cfg):
    """
    Front stop wall.
    """

    outer_width = cfg.gps_width + 2 * cfg.wall

    wall = box(
        outer_width,
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