"""
Reference GPS module.

Visual reference model for checking cradle fit.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
    fuse_all,
    feature,
)


def create_shape(cfg):
    """
    Create a simplified GPS module.

    PCB:
        22 x 22 x pcb_thickness

    Antenna:
        18 x 18
    """

    #
    # PCB
    #

    pcb = box(
        cfg.gps_width,
        cfg.gps_length,
        cfg.pcb_thickness,
    )

    #
    # Antenna block
    #

    antenna_height = cfg.gps_height - cfg.pcb_thickness

    antenna = box(
        cfg.antenna_width,
        cfg.antenna_length,
        antenna_height,
    )

    move(
        antenna,
        (cfg.gps_width - cfg.antenna_width) / 2,
        (cfg.gps_length - cfg.antenna_length) / 2,
        cfg.pcb_thickness,
    )

    return fuse_all([
        pcb,
        antenna,
    ])


def create(doc, parent, cfg):
    """
    Add GPS dummy into document.
    """

    shape = create_shape(cfg)

    #
    # Position inside cradle
    #

    move(
        shape,
        cfg.wall,
        cfg.wall,
        cfg.wall,
    )

    return feature(
        doc,
        parent,
        "GPS_Dummy",
        shape,
    )