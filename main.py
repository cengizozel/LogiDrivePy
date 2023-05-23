import tkinter as tk
import ctypes
import time


def initialize_functions(logi_dll):
    # Define the argument types and return type for the LogiSteeringInitialize function
    global LogiSteeringInitialize, LogiIsConnected, LogiUpdate, LogiPlaySpringForce

    LogiSteeringInitialize = logi_dll.LogiSteeringInitialize
    LogiSteeringInitialize.argtypes = [ctypes.c_bool]
    LogiSteeringInitialize.restype = ctypes.c_bool

    LogiIsConnected = logi_dll.LogiIsConnected
    LogiIsConnected.argtypes = [ctypes.c_int]
    LogiIsConnected.restype = ctypes.c_bool

    LogiUpdate = logi_dll.LogiUpdate
    LogiUpdate.argtypes = []
    LogiUpdate.restype = ctypes.c_bool

    LogiPlaySpringForce = logi_dll.LogiPlaySpringForce
    LogiPlaySpringForce.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    LogiPlaySpringForce.restype = ctypes.c_bool


root = tk.Tk()
root.withdraw()

dll_path = "dll/LogitechSteeringWheelEnginesWrapper.dll"
logi_dll = ctypes.cdll.LoadLibrary(dll_path)

initialize_functions(logi_dll)

ignore_xinput_controllers = True  # or False, depending on your needs
result = LogiSteeringInitialize(ignore_xinput_controllers)
print(f"\nLogiSteeringInitialize output: {result}\n")

for i in range(100):
    print(f"LogiUpdate output: {LogiUpdate()}", end=", ")
    print(f"LogiIsConnected output: {LogiIsConnected(0)}   ", end="\r")

    LogiPlaySpringForce(0, i, 100, 40)
    time.sleep(0.1)
    root.update()