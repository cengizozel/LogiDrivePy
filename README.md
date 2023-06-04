# LogiDrivePy - Logitech Controller Python Module

A Python module for interfacing with Logitech steering wheels. This module was tested with the Logitech G920 Driving Force Racing Wheel but should work with other Logitech devices as specified in the [Supported Devices](#supported-devices) section.

## Introduction

This Python module facilitates interaction with Logitech steering wheels, serving as a bridge between Python and the Logitech Steering Wheel's software components.

The original functionality was provided in the form of a C# implementation as part of the [Logitech Steering Wheel SDK](https://www.logitechg.com/en-us/innovation/developer-lab.html) for the [Unity Game Engine](https://assetstore.unity.com/packages/tools/integration/logitech-gaming-sdk-6630). The SDK allows developers to easily add Logitech steering wheel support to their games, using a set of predefined force feedback effects or creating custom effects by defining specific forces.

With the aim to extend these capabilities to the Python community, this module was developed as an accessible tool for Python developers. Utilizing the `ctypes` Python library, the module enables Python scripts to load and interact with Logitech steering wheels through Logitech's DLL (LogitechSteeringWheelEnginesWrapper.dll), providing a seamless integration experience for developers working with these devices.

## Supported Devices

This library was tested with the Logitech G920 Driving Force Racing Wheel, but according to Logitech documentation, it should also work with the following devices:

### Logitech
- G29
- G920
- Driving Force GT
- G27
- G25
- Driving Force Pro
- MOMO Force
- MOMO Racing
- Formula Force GP
- Driving Force
- Formula Force
- Force 3D
- Strike Force 3D
- Freedom 2.4 Cordless Joystick
- Cordless Rumblepad
- Cordless Rumblepad 2
- Rumblepad

### Microsoft
- Sidewinder Force Feedback 2 (Stick)
- Sidewinder Force (Wheel)

### Other (with Immersion drivers)
- Saitek Cyborg 3D Force
- Act-Labs Force RS Wheel

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

Please note that this project is *not* a reverse engineering of the Logitech Gaming Steering Wheel SDK. Instead, this project aims to provide an interface to Logitech steering wheels in Python by utilizing the SDK's provided DLL file (LogitechSteeringWheelEnginesWrapper.dll) without decompiling, disassembling, or otherwise altering the SDK's components. This project is designed to extend the functionality of the SDK for Python developers while respecting and complying with the original End-User License Agreement of the SDK.
