import tkinter as tk
import ctypes
import time


class LogitechController:
    def __init__(self, dll_path):
        self.dll_path = dll_path
        self.logi_dll = ctypes.cdll.LoadLibrary(dll_path)

        self.LogiSteeringInitialize = self.logi_dll.LogiSteeringInitialize
        self.LogiSteeringInitialize.argtypes = [ctypes.c_bool]
        self.LogiSteeringInitialize.restype = ctypes.c_bool

        self.LogiIsConnected = self.logi_dll.LogiIsConnected
        self.LogiIsConnected.argtypes = [ctypes.c_int]
        self.LogiIsConnected.restype = ctypes.c_bool

        self.LogiUpdate = self.logi_dll.LogiUpdate
        self.LogiUpdate.argtypes = []
        self.LogiUpdate.restype = ctypes.c_bool

        self.LogiPlaySpringForce = self.logi_dll.LogiPlaySpringForce
        self.LogiPlaySpringForce.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.LogiPlaySpringForce.restype = ctypes.c_bool

    def initialize(self, ignore_xinput_controllers=True):
        result = self.LogiSteeringInitialize(ignore_xinput_controllers)
        print(f"\nLogiSteeringInitialize output: {result}\n")

    def update(self, repetitions=100):
        root = tk.Tk()
        root.withdraw()

        for i in range(repetitions):
            print(f"LogiUpdate output: {self.LogiUpdate()}", end=", ")
            print(f"LogiIsConnected output: {self.LogiIsConnected(0)}   ", end="\r")

            self.LogiPlaySpringForce(0, i, 100, 40)
            time.sleep(0.1)
            root.update()


if __name__ == "__main__":
    dll_path = "dll/LogitechSteeringWheelEnginesWrapper.dll"
    controller = LogitechController(dll_path)
    controller.initialize()
    controller.update()
