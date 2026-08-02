"""
Creates a FreeCAD Spreadsheet from MountConfig.

Every field in MountConfig becomes one spreadsheet cell with the
same name, making the CAD model fully parametric.
"""

from __future__ import annotations

from dataclasses import fields

import FreeCAD as App

from config import MountConfig


def create_spreadsheet(doc, cfg: MountConfig):
    """
    Create a Spreadsheet object and populate it from MountConfig.

    Parameters
    ----------
    doc : App.Document
        Active FreeCAD document.

    cfg : MountConfig
        Configuration object.

    Returns
    -------
    Spreadsheet object
    """

    sheet = doc.addObject("Spreadsheet::Sheet", "Spreadsheet")

    row = 1

    for field in fields(cfg):

        # Column A = parameter name
        sheet.set("A{}".format(row), field.name)

        # Column B = value
        value = getattr(cfg, field.name)
        sheet.set("B{}".format(row), str(value))

        # Create spreadsheet alias
        try:
            sheet.setAlias("B{}".format(row), field.name)
        except Exception:
            # Ignore if alias already exists
            pass

        row += 1

    doc.recompute()

    return sheet