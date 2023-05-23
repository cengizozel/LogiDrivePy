# LogiDrivePy - Logitech Controller Python Module

A Python module for interfacing with Logitech Steering Wheel using the Logitech Steering Wheel Engine. This module was tested on a Logitech G920 Driving Force Racing Wheel.

## Introduction

This module is an implementation of the Logitech Steering Wheel Engine's interface. It uses the `ctypes` Python library to load and call functions from the Logitech's DLL (LogitechSteeringWheelEnginesWrapper.dll). This module provides an easy-to-use Pythonic interface allowing users to interact with the Logitech Steering Wheel.

## Installation

To install the package, clone the repository and use the `setup.py` file: 

```
git clone https://github.com/cengizozel/LogiDrivePy.git
cd LogiDrivePy
python setup.py install
```

Your project structure should look like this:

```
LogiDrivePy
│   .gitignore
│   LICENSE.txt
│   README.md
│   setup.py
│
├───logidrivepy
│   │   logitech_controller.py
│   │   __init__.py
│   │
│   ├───dll
│   │       LogitechSteeringWheelEnginesWrapper.dll
│
└───tests
        test.py
        __init__.py
```

## Usage

Here's a simple example on how to use the Logitech Controller module in your Python script.

```python
from logidrivepy import LogitechController

def main():
    dll_path = "logidrivepy/dll/LogitechSteeringWheelEnginesWrapper.dll"
    controller = LogitechController(dll_path)

    # Test initialization
    controller.initialize()

    # Give the controller some time to initialize
    time.sleep(1)

    # Test update
    controller.update(repetitions=100)

if __name__ == "__main__":
    main()
```