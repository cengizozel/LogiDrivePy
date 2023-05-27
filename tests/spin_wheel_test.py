import tkinter as tk
import time

# import sys
# sys.path.append('../logidrivepy')
from logidrivepy import LogitechController

def spin_test(controller):
    root = tk.Tk()
    root.withdraw()
    for i in range(-100, 102, 2):
        controller.LogiPlaySpringForce(0, i, 100, 40)
        controller.logi_update()
        
        time.sleep(0.1)
        root.update()
    root.destroy()

def test_logitech_controller():
    dll_path = "logidrivepy/dll/LogitechSteeringWheelEnginesWrapper.dll"
    controller = LogitechController(dll_path)

    controller.steering_initialize()
    print("\n---Logitech Spin Test---")
    spin_test(controller)
    print("Spin test passed.\n")

    controller.steering_shutdown()

if __name__ == "__main__":
    test_logitech_controller()
