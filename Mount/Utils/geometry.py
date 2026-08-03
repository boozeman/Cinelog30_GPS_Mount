"""
Common geometry helper functions.

These helpers wrap the FreeCAD Part API to keep the builders clean.
"""

from __future__ import annotations

import FreeCAD as App
import Part


# --------------------------------------------------
# Primitive geometry
# --------------------------------------------------

def box(x: float, y: float, z: float):
    """
    Create a rectangular box.
    """

    return Part.makeBox(x, y, z)


def cylinder(radius: float, height: float):
    """
    Create a cylinder.
    """

    return Part.makeCylinder(radius, height)


# --------------------------------------------------
# Transformations
# --------------------------------------------------

def move(shape, x=0.0, y=0.0, z=0.0):
    """
    Translate a shape.
    """

    shape.translate(App.Vector(x, y, z))

    return shape


# --------------------------------------------------
# Boolean operations
# --------------------------------------------------

def cut(base, tool):
    """
    Boolean subtraction.
    """

    return base.cut(tool)


def fuse(a, b):
    """
    Boolean union.
    """

    return a.fuse(b)


def fuse_all(parts):
    """
    Fuse a list of shapes into one.
    """

    if len(parts) == 0:
        raise ValueError("No parts supplied to fuse_all().")

    shape = parts[0]

    for part in parts[1:]:
        shape = fuse(shape, part)

    return shape