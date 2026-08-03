"""
Reference GPS module.

Visual reference model for checking cradle fit.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    move,
    fuse_all,
)

from body import add_feature

from Mount.GPSCradle.dimensions import (
    gps_x,
    gps_y,
    gps_z,
)


# --------------------------------------------------
# Shape
# --------------------------------------------------

def create_shape(cfg):
    """
    Create a simplified GPS module.

    PCB:
        gps_width × gps_length × pcb_thickness

    Antenna:
        antenna_width × antenna_length
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
    # Antenna
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


# --------------------------------------------------
# Builder
# --------------------------------------------------

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
        gps_x(cfg),
        gps_y(cfg),
        gps_z(cfg),
    )

    return add_feature(
        doc,
        parent,
        "GPS_Dummy",
        shape,
    )