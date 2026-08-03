"""
Creates the FreeCAD document and the root App::Part.
"""

from __future__ import annotations

import FreeCAD as App


def create_document(name: str = "CineLog30_GPS_Mount"):
    """
    Create a new document and the root Part container.

    Returns
    -------
    tuple(App.Document, App.Part)
        (document, root_part)
    """

    doc = App.newDocument(name)

    mount = doc.addObject("App::Part", "Mount")

    doc.recompute()

    return doc, mount

# --------------------------------------------------
# FreeCAD feature
# --------------------------------------------------

def feature(doc, parent, name: str, shape):
    """
    Create a Part::Feature in the document.
    """

    obj = doc.addObject("Part::Feature", name)

    obj.Shape = shape

    if parent is not None:
        parent.addObject(obj)

    doc.recompute()

    check(shape, name)

    return obj