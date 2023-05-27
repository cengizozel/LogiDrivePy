import ctypes

class LogitechControllerStructs:
    # Structs
    class LogiControllerPropertiesData(ctypes.Structure):
        _fields_ = [
            ("forceEnable", ctypes.c_bool),
            ("overallGain", ctypes.c_int),
            ("springGain", ctypes.c_int),
            ("damperGain", ctypes.c_int),
            ("defaultSpringEnabled", ctypes.c_bool),
            ("defaultSpringGain", ctypes.c_int),
            ("combinePedals", ctypes.c_bool),
            ("wheelRange", ctypes.c_int),
            ("gameSettingsEnabled", ctypes.c_bool),
            ("allowGameSettings", ctypes.c_bool)
        ]

    class DIJOYSTATE2ENGINES(ctypes.Structure):
        _fields_ = [
            ("lX", ctypes.c_int),
            ("lY", ctypes.c_int),
            ("lZ", ctypes.c_int),
            ("lRx", ctypes.c_int),
            ("lRy", ctypes.c_int),
            ("lRz", ctypes.c_int),
            ("rglSlider", ctypes.c_int * 2),
            ("rgdwPOV", ctypes.c_uint * 4),
            ("rgbButtons", ctypes.c_byte * 128),
            ("lVX", ctypes.c_int),
            ("lVY", ctypes.c_int),
            ("lVZ", ctypes.c_int),
            ("lVRx", ctypes.c_int),
            ("lVRy", ctypes.c_int),
            ("lVRz", ctypes.c_int),
            ("rglVSlider", ctypes.c_int * 2),
            ("lAX", ctypes.c_int),
            ("lAY", ctypes.c_int),
            ("lAZ", ctypes.c_int),
            ("lARx", ctypes.c_int),
            ("lARy", ctypes.c_int),
            ("lARz", ctypes.c_int),
            ("rglASlider", ctypes.c_int * 2),
            ("lFX", ctypes.c_int),
            ("lFY", ctypes.c_int),
            ("lFZ", ctypes.c_int),
            ("lFRx", ctypes.c_int),
            ("lFRy", ctypes.c_int),
            ("lFRz", ctypes.c_int),
            ("rglFSlider", ctypes.c_int * 2)
        ]
