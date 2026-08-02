"""
CineLog30 V3 GPS Mount

Main build script.
"""

from __future__ import annotations

import FreeCAD as App
import dev
import body
import spreadsheet
import config

from Mount.GPSCradle.builder import create as create_gps_cradle


def build():
    """
    Build complete model.
    """

    print("----------------------------------------")
    print(" CineLog30 V3 GPS Mount Builder")
    print("----------------------------------------")

    #
    # Configuration
    #

    cfg = config.MountConfig()

    #
    # Create document
    #

    doc, mount = body.create_document()

    #
    # Spreadsheet
    #

    spreadsheet.create_spreadsheet(doc, cfg)

    #
    # GPS cradle
    #

    create_gps_cradle(
        doc,
        mount,
        cfg,
    )

    #
    # Final recompute
    #

    doc.recompute()

    print("----------------------------------------")
    print("Build completed successfully")
    print(f"Objects: {len(doc.Objects)}")

    return doc


if __name__ == "__main__":
    build()