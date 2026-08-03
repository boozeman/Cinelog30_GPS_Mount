"""
Shared dimensions for the GPS cradle.

All geometry modules use these helper functions instead of calculating
dimensions themselves.
"""

from __future__ import annotations


# --------------------------------------------------
# GPS dimensions
# --------------------------------------------------

def gps_width(cfg):
    return cfg.gps_width


def gps_length(cfg):
    return cfg.gps_length


def gps_height(cfg):
    return cfg.gps_height


# --------------------------------------------------
# Internal dimensions
# --------------------------------------------------

def inner_width(cfg):
    """
    Free space inside cradle.
    """

    return gps_width(cfg) + 2 * cfg.fit_clearance


def inner_length(cfg):
    """
    Free space inside cradle.
    """

    return gps_length(cfg) + 2 * cfg.fit_clearance


def inner_height(cfg):

    return gps_height(cfg)


# --------------------------------------------------
# External dimensions
# --------------------------------------------------

def outer_width(cfg):

    return inner_width(cfg) + 2 * cfg.wall


def outer_length(cfg):

    return inner_length(cfg) + 2 * cfg.wall


def outer_height(cfg):

    return cfg.wall + inner_height(cfg)


# --------------------------------------------------
# Generic positioning helpers
# --------------------------------------------------

def center_x(cfg, width):

    return (outer_width(cfg) - width) / 2


def center_y(cfg, length):

    return (outer_length(cfg) - length) / 2


# --------------------------------------------------
# Reference planes
# --------------------------------------------------

def floor_z(cfg):

    return cfg.wall


def left_wall_x(cfg):

    return 0.0


def right_wall_x(cfg):

    return outer_width(cfg)


def front_wall_y(cfg):

    return 0.0


def back_wall_y(cfg):

    return outer_length(cfg)


# --------------------------------------------------
# GPS position
# --------------------------------------------------

def gps_x(cfg):

    return center_x(cfg, gps_width(cfg))


def gps_y(cfg):

    return center_y(cfg, gps_length(cfg))


def gps_z(cfg):

    return floor_z(cfg)


# --------------------------------------------------
# Rails
# --------------------------------------------------

def rail_length(cfg):

    return (
        inner_length(cfg)
        - cfg.rail_entry
        - cfg.rail_front_stop
    )


def left_rail_x(cfg):

    return cfg.wall


def right_rail_x(cfg):

    return outer_width(cfg) - cfg.wall - cfg.rail_width


def rail_y(cfg):

    return cfg.wall + cfg.rail_entry


def rail_z(cfg):

    return floor_z(cfg) + cfg.pcb_thickness


# --------------------------------------------------
# Connector
# --------------------------------------------------

def connector_x(cfg):

    return center_x(cfg, cfg.connector_width) + cfg.connector_offset


def connector_y(cfg):

    return (
        outer_length(cfg)
        - cfg.connector_depth
        - cfg.connector_from_back
    )