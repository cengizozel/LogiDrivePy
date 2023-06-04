import ctypes
import tkinter as tk

class LogitechControllerFunctions:
    def __init__(self, dll_path, structs, use_gui=True):
        self.structs = structs
        self.logi_dll = ctypes.cdll.LoadLibrary(dll_path)

        # If use_gui flag is True, then create a hidden Tkinter window
        if use_gui:
            self.root = tk.Tk()
            self.root.withdraw()
            self.root.update()

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
        self.LogiGetStateENGINES.restype = ctypes.POINTER(self.structs.DIJOYSTATE2ENGINES)

        def LogiGetStateCSharp(index):
            ret = self.structs.DIJOYSTATE2ENGINES()
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
        self.LogiSetPreferredControllerProperties.argtypes = [self.structs.LogiControllerPropertiesData]
        self.LogiSetPreferredControllerProperties.restype = ctypes.c_bool

        # LogiGetCurrentControllerProperties
        self.LogiGetCurrentControllerProperties = self.logi_dll.LogiGetCurrentControllerProperties
        self.LogiGetCurrentControllerProperties.argtypes = [ctypes.c_int, ctypes.POINTER(self.structs.LogiControllerPropertiesData)]
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

    def steering_initialize(self, ignore_xinput_controllers=True):
        return self.LogiSteeringInitialize(ignore_xinput_controllers)
    
    def logi_update(self):
        return self.LogiUpdate()
    
    def get_state_engines(self, index):
        return self.LogiGetStateENGINES(index)
    
    def get_device_path(self, index, str, size):
        return self.LogiGetDevicePath(index, str, size)
    
    def get_friendly_product_name(self, index, str, size):
        return self.LogiGetFriendlyProductName(index, str, size)
    
    def is_connected(self, index):
        return self.LogiIsConnected(index)
    
    def is_device_connected(self, index, device_type):
        return self.LogiIsDeviceConnected(index, device_type)
    
    def is_manufacturer_connected(self, index, manufacturer_name):
        return self.LogiIsManufacturerConnected(index, manufacturer_name)

    def is_model_connected(self, index, model_name):
        return self.LogiIsModelConnected(index, model_name)

    def button_triggered(self, index, button_number):
        return self.LogiButtonTriggered(index, button_number)

    def button_released(self, index, button_number):
        return self.LogiButtonReleased(index, button_number)

    def button_is_pressed(self, index, button_number):
        return self.LogiButtonIsPressed(index, button_number)

    def generate_non_linear_values(self, index, non_lin_coeff):
        return self.LogiGenerateNonLinearValues(index, non_lin_coeff)

    def get_non_linear_value(self, index, input_value):
        return self.LogiGetNonLinearValue(index, input_value)

    def has_force_feedback(self, index):
        return self.LogiHasForceFeedback(index)

    def is_playing(self, index, force_type):
        return self.LogiIsPlaying(index, force_type)

    def play_spring_force(self, index, offset_percentage, saturation_percentage, coefficient_percentage):
        return self.LogiPlaySpringForce(index, offset_percentage, saturation_percentage, coefficient_percentage)

    def stop_spring_force(self, index):
        return self.LogiStopSpringForce(index)

    def play_constant_force(self, index, magnitude_percentage):
        return self.LogiPlayConstantForce(index, magnitude_percentage)

    def stop_constant_force(self, index):
        return self.LogiStopConstantForce(index)

    def play_damper_force(self, index, coefficient_percentage):
        return self.LogiPlayDamperForce(index, coefficient_percentage)

    def stop_damper_force(self, index):
        return self.LogiStopDamperForce(index)

    def play_side_collision_force(self, index, magnitude_percentage):
        return self.LogiPlaySideCollisionForce(index, magnitude_percentage)

    def play_frontal_collision_force(self, index, magnitude_percentage):
        return self.LogiPlayFrontalCollisionForce(index, magnitude_percentage)

    def play_dirt_road_effect(self, index, magnitude_percentage):
        return self.LogiPlayDirtRoadEffect(index, magnitude_percentage)

    def stop_dirt_road_effect(self, index):
        return self.LogiStopDirtRoadEffect(index)

    def play_bumpy_road_effect(self, index, magnitude_percentage):
        return self.LogiPlayBumpyRoadEffect(index, magnitude_percentage)

    def stop_bumpy_road_effect(self, index):
        return self.LogiStopBumpyRoadEffect(index)

    def play_slippery_road_effect(self, index, magnitude_percentage):
        return self.LogiPlaySlipperyRoadEffect(index, magnitude_percentage)

    def stop_slippery_road_effect(self, index):
        return self.LogiStopSlipperyRoadEffect(index)

    def play_surface_effect(self, index, type, magnitude_percentage, period):
        return self.LogiPlaySurfaceEffect(index, type, magnitude_percentage, period)

    def stop_surface_effect(self, index):
        return self.LogiStopSurfaceEffect(index)

    def play_car_airborne(self, index):
        return self.LogiPlayCarAirborne(index)

    def stop_car_airborne(self, index):
        return self.LogiStopCarAirborne(index)

    def play_softstop_force(self, index, usable_range_percentage):
        return self.LogiPlaySoftstopForce(index, usable_range_percentage)

    def stop_softstop_force(self, index):
        return self.LogiStopSoftstopForce(index)

    def set_preferred_controller_properties(self, properties):
        return self.LogiSetPreferredControllerProperties(properties)

    def get_current_controller_properties(self, index, properties):
        return self.LogiGetCurrentControllerProperties(index, properties)

    def get_shifter_mode(self, index):
        return self.LogiGetShifterMode(index)

    def get_operating_range(self, index, range):
        return self.LogiGetOperatingRange(index, range)

    def set_operating_range(self, index, range):
        return self.LogiSetOperatingRange(index, range)

    def play_leds(self, index, current_rpm, rpm_first_led_turns_on, rpm_red_line):
        return self.LogiPlayLeds(index, current_rpm, rpm_first_led_turns_on, rpm_red_line)

    def steering_shutdown(self):
        # Destroy the GUI window if it exists
        if hasattr(self, 'root'):
            self.root.destroy()
        return self.LogiSteeringShutdown()
