"""
Development helper.

Reloads all project modules and builds the model.
"""
import sys

PROJECT = r"C:\Users\timov\git\Cinelog30_GPS_Mount"

if PROJECT not in sys.path:
    sys.path.insert(0, PROJECT)

print(sys.path[0])


import importlib

import config
import body
import spreadsheet
import build_mount

import Mount.Utils.geometry as geometry

import Mount.GPSCradle.base as base
import Mount.GPSCradle.walls as walls
import Mount.GPSCradle.connector as connector
import Mount.GPSCradle.builder as cradle_builder

import Mount.CameraMount.builder as arm_builder

DEBUG = True

def reload_all():

    modules = [

        geometry,

        base,
        walls,
        connector,
        cradle_builder,

        arm_builder,

        config,
        body,
        spreadsheet,
        build_mount,
    ]

    for module in modules:
        importlib.reload(module)

    print("All modules reloaded.")


def build():

    reload_all()

    return build_mount.build()

# --------------------------------------------------
# Debug
# --------------------------------------------------

def check(shape, name="Shape"):

    if not DEBUG:
        return

    print(
        f"{name}: "
        f"valid={shape.isValid()} "
        f"volume={shape.Volume:.2f}"
    )
