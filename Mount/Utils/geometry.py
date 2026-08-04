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


def cylinder(
    radius: float,
    height: float,
    axis: str = "z",
):
    """
    Create a cylinder.

    axis:
        "x"
        "y"
        "z"
    """

    directions = {
        "x": App.Vector(1, 0, 0),
        "y": App.Vector(0, 1, 0),
        "z": App.Vector(0, 0, 1),
    }

    return Part.makeCylinder(
        radius,
        height,
        App.Vector(0, 0, 0),
        directions[axis],
    )


# --------------------------------------------------
# Transformations
# --------------------------------------------------

def move(shape, x=0.0, y=0.0, z=0.0):
    """
    Translate a shape.
    """

    shape.translate(App.Vector(x, y, z))

    return shape


def rotate(shape, x=0.0, y=0.0, z=0.0):
    """
    Rotate a shape around the origin.
    Angles are in degrees.
    """

    if x:
        shape.rotate(
            App.Vector(0, 0, 0),
            App.Vector(1, 0, 0),
            x,
        )

    if y:
        shape.rotate(
            App.Vector(0, 0, 0),
            App.Vector(0, 1, 0),
            y,
        )

    if z:
        shape.rotate(
            App.Vector(0, 0, 0),
            App.Vector(0, 0, 1),
            z,
        )

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

    if not parts:
        raise ValueError("No parts supplied to fuse_all().")

    shape = parts[0]

    for part in parts[1:]:
        shape = fuse(shape, part)

    return shape


# --------------------------------------------------
# Edge operations
# --------------------------------------------------

def fillet(shape, radius, edges):
    """
    Apply a fillet to selected edges.

    edges = list of edge indices (1-based)
    """

    return shape.makeFillet(
        radius,
        [shape.Edges[i - 1] for i in edges],
    )


def chamfer(shape, distance, edges):
    """
    Apply a chamfer to selected edges.

    edges = list of edge indices (1-based)
    """

    return shape.makeChamfer(
        distance,
        [shape.Edges[i - 1] for i in edges],
    )