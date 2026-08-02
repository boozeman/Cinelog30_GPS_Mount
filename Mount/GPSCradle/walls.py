"""
GPS cradle walls.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
)


def _outer_width(cfg):
    return cfg.gps_width + 2 * cfg.wall


def _outer_length(cfg):
    return cfg.gps_length + 2 * cfg.wall


def create_left(cfg):
    """
    Left wall.
    """

    wall = box(
        cfg.wall,
        _outer_length(cfg),
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
        _outer_length(cfg),
        cfg.gps_height,
    )

    move(
        wall,
        _outer_width(cfg) - cfg.wall,
        0,
        cfg.wall,
    )

    return wall


def create_front(cfg):
    """
    Front stop wall.
    """

    wall = box(
        _outer_width(cfg),
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