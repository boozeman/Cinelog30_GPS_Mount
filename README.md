# CineLog30 GPS Mount

A fully parametric FreeCAD project for designing a lightweight GPS mount for the GEPRC CineLog30.

The project is written entirely in Python using the FreeCAD Part API. All dimensions are controlled from a single configuration object and automatically exported to a FreeCAD Spreadsheet for easy parameter editing.

---

## Features

- Fully parametric design
- Modular architecture
- Automatic FreeCAD Spreadsheet generation
- Configurable GPS module dimensions
- Adjustable assembly clearances
- Parametric PCB guide rails
- Parametric connector opening
- Reference GPS dummy model for fit verification

---

## Project Structure

```
Cinelog30_GPS_Mount/
│
├── build_mount.py          # Main build script
├── config.py               # All user-editable parameters
├── spreadsheet.py          # Creates FreeCAD Spreadsheet
├── body.py                 # FreeCAD document utilities
├── dev.py                  # Debug helpers
│
├── Mount/
│   ├── Utils/
│   │   └── geometry.py
│   │
│   ├── GPSCradle/
│   │   ├── builder.py
│   │   ├── dimensions.py
│   │   ├── base.py
│   │   ├── walls.py
│   │   ├── rails.py
│   │   └── connector.py
│   │
│   └── GoPro/
│       └── builder.py
│
└── Reference/
    └── gps_dummy.py
```

---

## Architecture

The project follows a modular design.

### config.py

Contains all user-editable parameters.

No geometry calculations should be placed here.

---

### dimensions.py

Calculates all derived dimensions and reference positions.

This is the single source of truth for geometry.

Examples:

- outer dimensions
- internal dimensions
- GPS position
- rail position
- connector position

Geometry modules should never calculate dimensions themselves.

---

### Geometry Modules

Each module is responsible for creating one logical part.

| Module | Responsibility |
|---------|----------------|
| base.py | Bottom plate |
| walls.py | Cradle walls |
| rails.py | PCB guide rails |
| connector.py | Connector and cable openings |

---

### builder.py

The builder assembles the cradle.

It does not create geometry itself.

Responsibilities:

- collect geometry
- fuse solids
- perform boolean cuts
- create the final FreeCAD feature

---

## Configuration

All dimensions are defined in

```
config.py
```

Changing values automatically affects the generated model.

Example:

```python
gps_width = 22.4
gps_length = 22.4
wall = 2.0
fit_clearance = 0.20
```

---

## Spreadsheet

During build, every configuration parameter is copied into a FreeCAD Spreadsheet.

This provides:

- easy inspection
- future GUI integration
- parameter documentation

---

## Building

Inside the FreeCAD Python console:

```python
import build_mount

build_mount.build()
```

---

## Design Goals

- clean architecture
- reusable geometry modules
- easy maintenance
- parametric design
- minimal duplicated calculations

---

## Current Status

Implemented:

- GPS cradle
- PCB rails
- Connector opening
- Cable slot
- Reference GPS model
- Automatic Spreadsheet generation

Planned:

- GoPro mount
- Support arm
- STL export helpers
- User interface