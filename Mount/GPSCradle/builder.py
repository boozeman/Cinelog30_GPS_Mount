"""
GPS Cradle Builder V1.0

Stage 1:
- Floor
- Four walls

No rails yet.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
    fuse_all,
    feature,
)

from Mount.GPSCradle.rail import (
    create_left,
    create_right,
)
print("builder.py loaded")

# --------------------------------------------------
# Base dimensions
# --------------------------------------------------


def outer_width(cfg):
    return cfg.gps_width + 2 * cfg.wall


def outer_length(cfg):
    return cfg.gps_length + 2 * cfg.wall


def outer_height(cfg):
    return cfg.gps_height + cfg.wall


# --------------------------------------------------
# Floor
# --------------------------------------------------


def create_floor(cfg):

    return box(
        outer_width(cfg),
        outer_length(cfg),
        cfg.wall,
    )


# --------------------------------------------------
# Left wall
# --------------------------------------------------


def create_left_wall(cfg):

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


# --------------------------------------------------
# Right wall
# --------------------------------------------------


def create_right_wall(cfg):

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


# --------------------------------------------------
# Front wall
# --------------------------------------------------


def create_front_wall(cfg):

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


# --------------------------------------------------
# Rear wall
# --------------------------------------------------


def create_back_wall(cfg):

    wall = box(
        outer_width(cfg),
        cfg.wall,
        cfg.gps_height,
    )

    move(
        wall,
        0,
        outer_length(cfg) - cfg.wall,
        cfg.wall,
    )

    return wall


# --------------------------------------------------
# Assemble
# --------------------------------------------------


def assemble(cfg):
    print("Assembling cradle")

    parts = [

        create_floor(cfg),

        create_left_wall(cfg),

        create_right_wall(cfg),

        create_front_wall(cfg),

        #create_back_wall(cfg),

        create_left(cfg),

        create_right(cfg),

    ]
    print(f"Parts: {len(parts)}")
    return fuse_all(parts)


# --------------------------------------------------
# Builder
# --------------------------------------------------


def create(doc, parent, cfg):

    print("Creating GPS cradle V1.0")

    shape = assemble(cfg)

    print("Valid :", shape.isValid())
    print("Volume:", shape.Volume)

    return feature(
        doc,
        parent,
        "GPS_Cradle",
        shape,
    )