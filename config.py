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

    gps_width: float = 22.4
    gps_length: float = 22.4
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
    connector_depth: float = 10.0
    connector_offset: float = 0.0
    connector_from_back: float = 0.0
    cable_hole_width: float = 8.0
    cable_hole_height: float = 8.0

    # --------------------------------------------------
    # GoPro arm
    # --------------------------------------------------

    arm_width: float = 10.0
    arm_height: float = 9.0
    arm_thickness: float = 5.0
    arm_angle_deg: float = 12.0

    # --------------------------------------------------
    # GoPro interface
    # --------------------------------------------------

    gopro_hole_diameter: float = 5.30

    finger_width: float = 8.0
    finger_gap: float = 3.20
    finger_thickness: float = 3.00

    # --------------------------------------------------
    # Fillets
    # --------------------------------------------------

    outer_fillet: float = 1.50
    finger_fillet: float = 2.00

    # --------------------------------------------------
    # Fit clearances
    # --------------------------------------------------  

    fit_clearance: float = 0.20