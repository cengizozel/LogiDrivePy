# LogiDrivePy - Logitech Controller Python Module

A Python module for interfacing with a Logitech steering wheel. This module was tested on a Logitech G920 Driving Force Racing Wheel.

## Introduction

This Python module facilitates interaction with the Logitech G920 Driving Force Racing Wheel, serving as a bridge between Python and the Logitech Steering Wheel's software components.

The original functionality was provided in the form of a C# implementation as part of the Logitech Steering Wheel SDK (Software Development Kit) for the Unity Game Engine, designed by Logitech's developers. The SDK includes APIs (Application Programming Interfaces), which are sets of protocols and tools that allow developers to interact with Logitech's steering wheel hardware.

Seeing the potential to extend this functionality to the Python community, this module was developed to enable the same capabilities for Python developers. By utilizing the `ctypes` Python library, the module can load and call functions from Logitech's DLL (LogitechSteeringWheelEnginesWrapper.dll), effectively enabling Python scripts to control and interact with the Logitech G920 Driving Force Racing Wheel.

## Installation

To install the package, simply use pip:
```
pip install logidrivepy
```

The package directory layout is organized as follows:
```
LogiDrivePy
|   .gitignore
|   LICENSE.txt
|   README.md
|   setup.py
|
+---logidrivepy
|   |   constants.py
|   |   controller.py
|   |   functions.py
|   |   structs.py
|   |   __init__.py
|   |
|   +---dll
|   |       LogitechSteeringWheelEnginesWrapper.dll
|
+---tests
    |   run_controller_test.py
    |   spin_wheel_test.py
    |   __init__.py
```

## Usage

Here's a simple example on how to use the Logitech Controller module in your Python script.

```python
from logidrivepy import LogitechController

controller = LogitechController()

print(f"steering_initialize: {controller.steering_initialize()}")
print(f"logi_update: {controller.logi_update()}")
print(f"is_connected: {controller.is_connected(0)}")

controller.steering_shutdown()
```

## Dependencies

This library uses the `ctypes` Python library to load and call functions from the Logitech's DLL (LogitechSteeringWheelEnginesWrapper.dll). The ctypes library is part of the standard Python library and should be installed by default with a standard Python installation.

This library also requires `Tkinter`, a Python binding to the Tk GUI toolkit. Tkinter is part of the standard Python library for Python 3 and should be installed by default with a standard Python installation.

### License

This project is licensed under the terms of the MIT license. For more details, see the `LICENSE.txt` file.
