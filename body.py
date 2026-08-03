"""
FreeCAD document utilities.
"""

from __future__ import annotations

import FreeCAD as App


# --------------------------------------------------
# Document
# --------------------------------------------------

def create_document(name="CineLog30_GPS_Mount"):
    """
    Create a new FreeCAD document and Part container.

    Returns
    -------
    (doc, part)
    """

    doc = App.newDocument(name)

    part = doc.addObject(
        "App::Part",
        "Mount",
    )

    doc.recompute()

    return doc, part


# --------------------------------------------------
# Features
# --------------------------------------------------

def add_feature(doc, parent, name, shape):
    """
    Add a Part::Feature to the document.

    Parameters
    ----------
    doc : App.Document
        Active FreeCAD document.

    parent : App::Part or None
        Parent container.

    name : str
        Object name.

    shape : Part.Shape
        Shape to assign.

    Returns
    -------
    App.DocumentObject
    """

    obj = doc.addObject(
        "Part::Feature",
        name,
    )

    if parent is not None:
        parent.addObject(obj)

    obj.Shape = shape

    doc.recompute()

    return obj