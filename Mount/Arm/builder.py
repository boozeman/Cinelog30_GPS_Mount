"""
Support Arm Builder

Assembles the support arm.
"""

from __future__ import annotations

from body import add_feature

from Mount.Arm import base


# --------------------------------------------------
# Assemble
# --------------------------------------------------

def assemble(cfg):
    """
    Assemble the support arm.
    """

    return base.create(cfg)


# --------------------------------------------------
# Builder
# --------------------------------------------------

def create(doc, parent, cfg):
    """
    Create the support arm.
    """

    print("Creating support arm")

    shape = assemble(cfg)

    return add_feature(
        doc,
        parent,
        "Support_Arm",
        shape,
    )