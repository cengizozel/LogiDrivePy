import tkinter as tk
import ctypes
import time


class LogitechController:
    def __init__(self, dll_path):
        self.dll_path = dll_path
        self.logi_dll = ctypes.cdll.LoadLibrary(dll_path)

        # CONSTANTS
        self.LOGI_MAX_CONTROLLERS = 4
       
        # Force types
        self.LOGI_FORCE_NONE = -1
        self.LOGI_FORCE_SPRING = 0
        self.LOGI_FORCE_CONSTANT = 1
        self.LOGI_FORCE_DAMPER = 2
        self.LOGI_FORCE_SIDE_COLLISION = 3
        self.LOGI_FORCE_FRONTAL_COLLISION = 4
        self.LOGI_FORCE_DIRT_ROAD = 5
        self.LOGI_FORCE_BUMPY_ROAD = 6
        self.LOGI_FORCE_SLIPPERY_ROAD = 7
        self.LOGI_FORCE_SURFACE_EFFECT = 8
        self.LOGI_NUMBER_FORCE_EFFECTS = 9
        self.LOGI_FORCE_SOFTSTOP = 10
        self.LOGI_FORCE_CAR_AIRBORNE = 11

        # Periodic types for surface effect
        self.LOGI_PERIODICTYPE_NONE = -1
        self.LOGI_PERIODICTYPE_SINE = 0
        self.LOGI_PERIODICTYPE_SQUARE = 1
        self.LOGI_PERIODICTYPE_TRIANGLE = 2

        # Device types
        self.LOGI_DEVICE_TYPE_NONE = -1
        self.LOGI_DEVICE_TYPE_WHEEL = 0
        self.LOGI_DEVICE_TYPE_JOYSTICK = 1
        self.LOGI_DEVICE_TYPE_GAMEPAD = 2
        self.LOGI_DEVICE_TYPE_OTHER = 3
        self.LOGI_NUMBER_DEVICE_TYPES = 4

        # Manufacturer types
        self.LOGI_MANUFACTURER_NONE = -1
        self.LOGI_MANUFACTURER_LOGITECH = 0
        self.LOGI_MANUFACTURER_MICROSOFT = 1
        self.LOGI_MANUFACTURER_OTHER = 2

        # Model types
        self.LOGI_MODEL_G27 = 0
        self.LOGI_MODEL_DRIVING_FORCE_GT = 1
        self.LOGI_MODEL_G25 = 2
        self.LOGI_MODEL_MOMO_RACING = 3
        self.LOGI_MODEL_MOMO_FORCE = 4
        self.LOGI_MODEL_DRIVING_FORCE_PRO = 5
        self.LOGI_MODEL_DRIVING_FORCE = 6
        self.LOGI_MODEL_NASCAR_RACING_WHEEL = 7
        self.LOGI_MODEL_FORMULA_FORCE = 8
        self.LOGI_MODEL_FORMULA_FORCE_GP = 9
        self.LOGI_MODEL_FORCE_3D_PRO = 10
        self.LOGI_MODEL_EXTREME_3D_PRO = 11
        self.LOGI_MODEL_FREEDOM_24 = 12
        self.LOGI_MODEL_ATTACK_3 = 13
        self.LOGI_MODEL_FORCE_3D = 14
        self.LOGI_MODEL_STRIKE_FORCE_3D = 15
        self.LOGI_MODEL_G940_JOYSTICK = 16
        self.LOGI_MODEL_G940_THROTTLE = 17
        self.LOGI_MODEL_G940_PEDALS = 18
        self.LOGI_MODEL_RUMBLEPAD = 19
        self.LOGI_MODEL_RUMBLEPAD_2 = 20
        self.LOGI_MODEL_CORDLESS_RUMBLEPAD_2 = 21
        self.LOGI_MODEL_CORDLESS_GAMEPAD = 22
        self.LOGI_MODEL_DUAL_ACTION_GAMEPAD = 23
        self.LOGI_MODEL_PRECISION_GAMEPAD_2 = 24
        self.LOGI_MODEL_CHILLSTREAM = 25
        self.LOGI_MODEL_G29 = 26
        self.LOGI_MODEL_G920 = 27
        self.LOGI_NUMBER_MODELS = 28

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

        # Function Definitions

        # LogiSteeringInitialize
        self.LogiSteeringInitialize = self.logi_dll.LogiSteeringInitialize
        self.LogiSteeringInitialize.argtypes = [ctypes.c_bool]
        self.LogiSteeringInitialize.restype = ctypes.c_bool

        # LogiUpdate
        self.LogiUpdate = self.logi_dll.LogiUpdate
        self.LogiUpdate.argtypes = []
        self.LogiUpdate.restype = ctypes.c_bool

        # LogiGetStateENGINES
        self.LogiGetStateENGINES = self.logi_dll.LogiGetStateENGINES
        self.LogiGetStateENGINES.argtypes = [ctypes.c_int]
        self.LogiGetStateENGINES.restype = ctypes.POINTER(DIJOYSTATE2ENGINES)

        def LogiGetStateCSharp(index):
            ret = DIJOYSTATE2ENGINES()
            ret.rglSlider = (ctypes.c_int * 2)()
            ret.rgdwPOV = (ctypes.c_uint * 4)()
            ret.rgbButtons = (ctypes.c_byte * 128)()
            ret.rglVSlider = (ctypes.c_int * 2)()
            ret.rglASlider = (ctypes.c_int * 2)()
            ret.rglFSlider = (ctypes.c_int * 2)()
            try:
                ret = self.LogiGetStateENGINES(index).contents
            except ctypes.ArgumentError:
                pass
            return ret

        # LogiGetDevicePath
        self.LogiGetDevicePath = self.logi_dll.LogiGetDevicePath
        self.LogiGetDevicePath.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
        self.LogiGetDevicePath.restype = ctypes.c_bool

        # LogiGetFriendlyProductName
        self.LogiGetFriendlyProductName = self.logi_dll.LogiGetFriendlyProductName
        self.LogiGetFriendlyProductName.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
        self.LogiGetFriendlyProductName.restype = ctypes.c_bool

        # LogiIsConnected
        self.LogiIsConnected = self.logi_dll.LogiIsConnected
        self.LogiIsConnected.argtypes = [ctypes.c_int]
        self.LogiIsConnected.restype = ctypes.c_bool

        # LogiIsDeviceConnected
        self.LogiIsDeviceConnected = self.logi_dll.LogiIsDeviceConnected
        self.LogiIsDeviceConnected.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiIsDeviceConnected.restype = ctypes.c_bool

        # LogiIsManufacturerConnected
        self.LogiIsManufacturerConnected = self.logi_dll.LogiIsManufacturerConnected
        self.LogiIsManufacturerConnected.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiIsManufacturerConnected.restype = ctypes.c_bool

        # LogiIsModelConnected
        self.LogiIsModelConnected = self.logi_dll.LogiIsModelConnected
        self.LogiIsModelConnected.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiIsModelConnected.restype = ctypes.c_bool

        # LogiButtonTriggered
        self.LogiButtonTriggered = self.logi_dll.LogiButtonTriggered
        self.LogiButtonTriggered.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiButtonTriggered.restype = ctypes.c_bool

        # LogiButtonReleased
        self.LogiButtonReleased = self.logi_dll.LogiButtonReleased
        self.LogiButtonReleased.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiButtonReleased.restype = ctypes.c_bool

        # LogiButtonIsPressed
        self.LogiButtonIsPressed = self.logi_dll.LogiButtonIsPressed
        self.LogiButtonIsPressed.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiButtonIsPressed.restype = ctypes.c_bool

        # LogiGenerateNonLinearValues
        self.LogiGenerateNonLinearValues = self.logi_dll.LogiGenerateNonLinearValues
        self.LogiGenerateNonLinearValues.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiGenerateNonLinearValues.restype = ctypes.c_bool

        # LogiGetNonLinearValue
        self.LogiGetNonLinearValue = self.logi_dll.LogiGetNonLinearValue
        self.LogiGetNonLinearValue.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiGetNonLinearValue.restype = ctypes.c_int

        # LogiHasForceFeedback
        self.LogiHasForceFeedback = self.logi_dll.LogiHasForceFeedback
        self.LogiHasForceFeedback.argtypes = [ctypes.c_int]
        self.LogiHasForceFeedback.restype = ctypes.c_bool

        # LogiIsPlaying
        self.LogiIsPlaying = self.logi_dll.LogiIsPlaying
        self.LogiIsPlaying.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiIsPlaying.restype = ctypes.c_bool

        # LogiPlaySpringForce
        self.LogiPlaySpringForce = self.logi_dll.LogiPlaySpringForce
        self.LogiPlaySpringForce.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.LogiPlaySpringForce.restype = ctypes.c_bool

        # LogiStopSpringForce
        self.LogiStopSpringForce = self.logi_dll.LogiStopSpringForce
        self.LogiStopSpringForce.argtypes = [ctypes.c_int]
        self.LogiStopSpringForce.restype = ctypes.c_bool

        # LogiPlayConstantForce
        self.LogiPlayConstantForce = self.logi_dll.LogiPlayConstantForce
        self.LogiPlayConstantForce.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiPlayConstantForce.restype = ctypes.c_bool

        # LogiStopConstantForce
        self.LogiStopConstantForce = self.logi_dll.LogiStopConstantForce
        self.LogiStopConstantForce.argtypes = [ctypes.c_int]
        self.LogiStopConstantForce.restype = ctypes.c_bool

        # LogiPlayDamperForce
        self.LogiPlayDamperForce = self.logi_dll.LogiPlayDamperForce
        self.LogiPlayDamperForce.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiPlayDamperForce.restype = ctypes.c_bool

        # LogiStopDamperForce
        self.LogiStopDamperForce = self.logi_dll.LogiStopDamperForce
        self.LogiStopDamperForce.argtypes = [ctypes.c_int]
        self.LogiStopDamperForce.restype = ctypes.c_bool

        # LogiPlaySideCollisionForce
        self.LogiPlaySideCollisionForce = self.logi_dll.LogiPlaySideCollisionForce
        self.LogiPlaySideCollisionForce.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiPlaySideCollisionForce.restype = ctypes.c_bool

        # LogiPlayFrontalCollisionForce
        self.LogiPlayFrontalCollisionForce = self.logi_dll.LogiPlayFrontalCollisionForce
        self.LogiPlayFrontalCollisionForce.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiPlayFrontalCollisionForce.restype = ctypes.c_bool

        # LogiPlayDirtRoadEffect
        self.LogiPlayDirtRoadEffect = self.logi_dll.LogiPlayDirtRoadEffect
        self.LogiPlayDirtRoadEffect.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiPlayDirtRoadEffect.restype = ctypes.c_bool

        # LogiStopDirtRoadEffect
        self.LogiStopDirtRoadEffect = self.logi_dll.LogiStopDirtRoadEffect
        self.LogiStopDirtRoadEffect.argtypes = [ctypes.c_int]
        self.LogiStopDirtRoadEffect.restype = ctypes.c_bool

        # LogiPlayBumpyRoadEffect
        self.LogiPlayBumpyRoadEffect = self.logi_dll.LogiPlayBumpyRoadEffect
        self.LogiPlayBumpyRoadEffect.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiPlayBumpyRoadEffect.restype = ctypes.c_bool

        # LogiStopBumpyRoadEffect
        self.LogiStopBumpyRoadEffect = self.logi_dll.LogiStopBumpyRoadEffect
        self.LogiStopBumpyRoadEffect.argtypes = [ctypes.c_int]
        self.LogiStopBumpyRoadEffect.restype = ctypes.c_bool

        # LogiPlaySlipperyRoadEffect
        self.LogiPlaySlipperyRoadEffect = self.logi_dll.LogiPlaySlipperyRoadEffect
        self.LogiPlaySlipperyRoadEffect.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiPlaySlipperyRoadEffect.restype = ctypes.c_bool

        # LogiStopSlipperyRoadEffect
        self.LogiStopSlipperyRoadEffect = self.logi_dll.LogiStopSlipperyRoadEffect
        self.LogiStopSlipperyRoadEffect.argtypes = [ctypes.c_int]
        self.LogiStopSlipperyRoadEffect.restype = ctypes.c_bool

        # LogiPlaySurfaceEffect
        self.LogiPlaySurfaceEffect = self.logi_dll.LogiPlaySurfaceEffect
        self.LogiPlaySurfaceEffect.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.LogiPlaySurfaceEffect.restype = ctypes.c_bool

        # LogiStopSurfaceEffect
        self.LogiStopSurfaceEffect = self.logi_dll.LogiStopSurfaceEffect
        self.LogiStopSurfaceEffect.argtypes = [ctypes.c_int]
        self.LogiStopSurfaceEffect.restype = ctypes.c_bool

        # LogiPlayCarAirborne
        self.LogiPlayCarAirborne = self.logi_dll.LogiPlayCarAirborne
        self.LogiPlayCarAirborne.argtypes = [ctypes.c_int]
        self.LogiPlayCarAirborne.restype = ctypes.c_bool

        # LogiStopCarAirborne
        self.LogiStopCarAirborne = self.logi_dll.LogiStopCarAirborne
        self.LogiStopCarAirborne.argtypes = [ctypes.c_int]
        self.LogiStopCarAirborne.restype = ctypes.c_bool

        # LogiPlaySoftstopForce
        self.LogiPlaySoftstopForce = self.logi_dll.LogiPlaySoftstopForce
        self.LogiPlaySoftstopForce.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiPlaySoftstopForce.restype = ctypes.c_bool

        # LogiStopSoftstopForce
        self.LogiStopSoftstopForce = self.logi_dll.LogiStopSoftstopForce
        self.LogiStopSoftstopForce.argtypes = [ctypes.c_int]
        self.LogiStopSoftstopForce.restype = ctypes.c_bool

        # LogiSetPreferredControllerProperties
        self.LogiSetPreferredControllerProperties = self.logi_dll.LogiSetPreferredControllerProperties
        self.LogiSetPreferredControllerProperties.argtypes = [LogiControllerPropertiesData]
        self.LogiSetPreferredControllerProperties.restype = ctypes.c_bool

        # LogiGetCurrentControllerProperties
        self.LogiGetCurrentControllerProperties = self.logi_dll.LogiGetCurrentControllerProperties
        self.LogiGetCurrentControllerProperties.argtypes = [ctypes.c_int, ctypes.POINTER(LogiControllerPropertiesData)]
        self.LogiGetCurrentControllerProperties.restype = ctypes.c_bool

        # LogiGetShifterMode
        self.LogiGetShifterMode = self.logi_dll.LogiGetShifterMode
        self.LogiGetShifterMode.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        self.LogiGetShifterMode.restype = ctypes.c_bool

        # LogiGetOperatingRange
        self.LogiGetOperatingRange = self.logi_dll.LogiGetOperatingRange
        self.LogiGetOperatingRange.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        self.LogiGetOperatingRange.restype = ctypes.c_bool

        # LogiSetOperatingRange
        self.LogiSetOperatingRange = self.logi_dll.LogiSetOperatingRange
        self.LogiSetOperatingRange.argtypes = [ctypes.c_int, ctypes.c_int]
        self.LogiSetOperatingRange.restype = ctypes.c_bool

        # LogiPlayLeds
        self.LogiPlayLeds = self.logi_dll.LogiPlayLeds
        self.LogiPlayLeds.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float]
        self.LogiPlayLeds.restype = ctypes.c_bool

        # LogiSteeringShutdown
        self.LogiSteeringShutdown = self.logi_dll.LogiSteeringShutdown
        self.LogiSteeringShutdown.argtypes = []
        self.LogiSteeringShutdown.restype = None

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
