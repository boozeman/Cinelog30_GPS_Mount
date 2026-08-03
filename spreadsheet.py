"""
Creates a FreeCAD Spreadsheet from MountConfig.

Every field in MountConfig becomes one spreadsheet cell with the
same name, making the CAD model fully parametric.
"""

from __future__ import annotations

from dataclasses import fields

from config import MountConfig


def create_spreadsheet(doc, cfg: MountConfig):
    """
    Create or update the project spreadsheet.
    """

    sheet = doc.getObject("Spreadsheet")

    if sheet is None:
        sheet = doc.addObject("Spreadsheet::Sheet", "Spreadsheet")

    row = 1

    for field in fields(cfg):

        value = getattr(cfg, field.name)

        sheet.set(f"A{row}", field.name)
        sheet.set(f"B{row}", str(value))

        try:
            sheet.setAlias(f"B{row}", field.name)
        except Exception:
            pass

        row += 1

    doc.recompute()

    return sheet