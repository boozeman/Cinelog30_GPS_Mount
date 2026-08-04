"""
Configuration for the CineLog30 V3 GPS mount.

All dimensions are in millimetres.
"""

from dataclasses import dataclass


@dataclass
class MountConfig:

    # --------------------------------------------------
    # GPS module
    # --------------------------------------------------

    gps_width: float = 22.0
    gps_length: float = 22.0
    gps_height: float = 8.2

    pcb_thickness: float = 0.8

    antenna_width: float = 18.0
    antenna_length: float = 18.0

    gps_clearance: float = 0.20

    # --------------------------------------------------
    # Cradle
    # --------------------------------------------------

    wall: float = 2.0

    # --------------------------------------------------
    # Slide profile
    # --------------------------------------------------

    rail_width: float = 1.4
    rail_height: float = 2.0
    rail_clearance: float = 0.20

    rail_length: float = 18.0
    rail_entry: float = 3.0
    rail_front_stop: float = 1.0

    # --------------------------------------------------
    # Connector
    # --------------------------------------------------

    connector_width: float = 10.0
    connector_height: float = 6.0
    connector_depth: float = 6.0
    connector_offset: float = 0.0
    connector_from_back: float = 0.0
    cable_hole_width: float = 10.0
    cable_hole_height: float = 10.0

    # --------------------------------------------------
    # Camera mount
    # --------------------------------------------------

    finger_height = 10.5

    outer_finger_width = 3.0
    center_finger_width = 5.2

    mount_clearance = 0.20

    finger_hole_diameter = 2.0
    finger_hole_from_tip = 3.2

    # --------------------------------------------------
    # Fillets
    # --------------------------------------------------

    outer_fillet: float = 1.50
    finger_fillet: float = 2.00

    # --------------------------------------------------
    # Fit clearances
    # --------------------------------------------------  

    fit_clearance: float = 0.20