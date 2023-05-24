import sys
import time

sys.path.append('..\\logidrivepy')

from logidrivepy import LogitechController

def test_logitech_controller():
    dll_path = "logidrivepy/dll/LogitechSteeringWheelEnginesWrapper.dll"
    controller = LogitechController(dll_path)

    # Test initialization
    controller.initialize()

    # Give the controller some time to initialize
    time.sleep(1)

    # Test update
    controller.update(repetitions=100)

    print("All tests passed.")

if __name__ == "__main__":
    test_logitech_controller()
