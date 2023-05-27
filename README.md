# LogiDrivePy - Logitech Controller Python Module

A Python module for interfacing with Logitech Steering Wheel using the Logitech Steering Wheel Engine. This module was tested on a Logitech G920 Driving Force Racing Wheel.

## Introduction

This module is an implementation of the Logitech Steering Wheel Engine's interface. It uses the `ctypes` Python library to load and call functions from the Logitech's DLL (LogitechSteeringWheelEnginesWrapper.dll). This module provides an easy-to-use Pythonic interface allowing users to interact with the Logitech Steering Wheel.

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
import tkinter as tk
from logidrivepy import LogitechController

def main():
    root = tk.Tk()
    root.withdraw()
    root.update()

    dll_path = "logidrivepy/dll/LogitechSteeringWheelEnginesWrapper.dll"
    controller = LogitechController(dll_path)
    
    steering_initialize = controller.steering_initialize()
    logi_update = controller.logi_update()
    is_connected = controller.is_connected(0)

    print(f"\n---Logitech Controller Test---")
    print(f"steering_initialize: {steering_initialize}")
    print(f"logi_update: {logi_update}")
    print(f"is_connected: {is_connected}")

    if steering_initialize and logi_update and is_connected:
        print(f"All tests passed.\n")
    else:
        print(f"Did not pass all tests.\n")

    controller.steering_shutdown()
    root.destroy()

if __name__ == "__main__":
    main()
```