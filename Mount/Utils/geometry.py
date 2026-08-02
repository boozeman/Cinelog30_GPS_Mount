"""
Common geometry helper functions.

These helpers wrap the FreeCAD Part API to keep the builders clean.
"""

from __future__ import annotations
from turtle import shape

import FreeCAD as App
import Part

def check(shape, name):
    print(f"{name}: valid={shape.isValid()} volume={shape.Volume}")

def box(x: float, y: float, z: float):
    """
    Create a box.

    Parameters
    ----------
    x, y, z : float
        Dimensions in millimetres.
    """

    return Part.makeBox(x, y, z)


def cylinder(radius: float, height: float):
    """
    Create a cylinder.
    """

    return Part.makeCylinder(radius, height)


def move(shape, x=0.0, y=0.0, z=0.0):
    """
    Move a shape.
    """

    shape.translate(App.Vector(x, y, z))

    return shape


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
    Fuse a list of Part shapes into a single shape.
    """

    if not parts:
        raise ValueError("parts list is empty")

    shape = parts[0]

    for part in parts[1:]:
        shape = shape.fuse(part)

    return shape

def feature(doc, parent, name: str, shape):

    obj = doc.addObject("Part::Feature", name)

    if parent is not None:
        parent.addObject(obj)

    obj.Shape = shape

    doc.recompute()

    print("Shape valid:", shape.isValid())
    print("Shape volume:", shape.Volume)
    print("Bounding box:", shape.BoundBox)

    return obj