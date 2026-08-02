"""
CineLog30 V3 GPS Mount

Main build script.

Run this file from FreeCAD to generate the complete model.
"""

from __future__ import annotations
from pydoc import doc

import FreeCAD as App

import body
import spreadsheet
import config

from Mount.GPSCradle.builder import create as create_gps_cradle


def build():
    """
    Build the complete CAD model.
    """

    print("----------------------------------------")
    print(" CineLog30 V3 GPS Mount Builder")
    print("----------------------------------------")

    cfg = config.MountConfig()

    doc, mount = body.create_document()

    sheet = spreadsheet.create_spreadsheet(doc, cfg)

    create_gps_cradle(doc, mount, cfg)

    doc.recompute()

    print("Build completed successfully.")
    print(f"Objects in document: {len(doc.Objects)}")    
    
    return doc


if __name__ == "__main__":

    build()

