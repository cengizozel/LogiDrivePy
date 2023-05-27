import tkinter as tk

# import sys
# sys.path.append('../logidrivepy')
from logidrivepy import LogitechController

if __name__ == "__main__":
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
