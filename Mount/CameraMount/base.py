"""
Camera mount base.

Creates the three mounting fingers.
"""

from __future__ import annotations

from Mount.Utils.geometry import (
    box,
    cylinder,
    move,
    fuse_all,
    cut,
    print_edges,
    fillet,
)

from Mount.CameraMount.dimensions import (
    finger_height,
    finger_length,
    outer_finger_width,
    center_finger_width,
    left_finger_x,
    center_finger_x,
    right_finger_x,
    hole_length,
    finger_hole_diameter,
    finger_hole_from_tip,
    hole_x,
    hole_y,
    hole_z,
 
)


def create(cfg):
    """
    Create camera mount geometry.

    Geometry is created at the origin.
    """
    print("finger_length =", finger_length(cfg))
    print("finger_height =", finger_height(cfg))
    print("center_width =", center_finger_width(cfg))  

    parts = []

    
    # Common finger coordinates
    
    finger_y = 0.0
    finger_z = -finger_height(cfg)

    # Left finger
    finger = box(
        outer_finger_width(cfg),
        finger_length(cfg),
        finger_height(cfg),
    )
    # round the tip of the finger
    finger = fillet(
        finger,
        1.5,
        [11, 12],
    )
    # Move finger to position
    move(
        finger,
        left_finger_x(cfg),
        finger_y,
        finger_z,
    )

    # Print finger BoundBox
    parts.append(finger)

    # Center finger
    finger = box(
        center_finger_width(cfg),
        finger_length(cfg),
        finger_height(cfg),
    )
    # round the tip of the finger
    finger = fillet(
        finger,
        1.5,
        [11, 12],
    )
    # Move finger to position
    move(
        finger,
        center_finger_x(cfg),
        finger_y,
        finger_z,
    )

    print_edges(finger)
    bb = finger.BoundBox

    print("Center finger BoundBox")
    print(f"X: {bb.XMin:.2f} -> {bb.XMax:.2f} ({bb.XLength:.2f})")
    print(f"Y: {bb.YMin:.2f} -> {bb.YMax:.2f} ({bb.YLength:.2f})")
    print(f"Z: {bb.ZMin:.2f} -> {bb.ZMax:.2f} ({bb.ZLength:.2f})")

    # print finger BoundBox 
    parts.append(finger)

    # Right finger
    finger = box(
        outer_finger_width(cfg),
        finger_length(cfg),
        finger_height(cfg),
    )
    # round the tip of the finger
    finger = fillet(
        finger,
        1.5,
        [11, 12],
    )
    # Move finger to position
    move(
        finger,
        right_finger_x(cfg),
        finger_y,
        finger_z,
    )

    # Print finger BoundBox
    parts.append(finger)

    # fuse all fingers into a single shape
    shape = fuse_all(parts)

    # camera mount hole
    hole = cylinder(
        finger_hole_diameter(cfg) / 2,
        hole_length(cfg),
        axis="x",
    )
    # Move hole to position
    move(
        hole,
        hole_x(cfg),
        hole_y(cfg),
        hole_z(cfg),
    )

    bb = hole.BoundBox

    print(
        "Hole center:",
        center_finger_x(cfg) + center_finger_width(cfg) / 2,
        finger_y + finger_length(cfg) - finger_hole_from_tip(cfg),
        finger_z + finger_height(cfg) / 2,
    )

    # cut hole from shape
    shape = cut(
        shape,
        hole,
    )

    return shape