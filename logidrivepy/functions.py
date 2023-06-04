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
        """
        Initializes the steering system if certain conditions are met.

        Args:
            - ignore_xinput_controllers (bool, optional): If true, X-input controllers are ignored. Default is True.

        Returns:
            - bool: Returns True if:
                * No other instance is running, and
                * The main window is in the foreground.
            Otherwise, returns False.

        Note:
            - This is a part of the Logitech G Hub APIs. Make sure to install the necessary drivers and libraries.

        Example:
            >>> steering_initialize(ignore_xinput_controllers=False)
        """
        return self.LogiSteeringInitialize(ignore_xinput_controllers)
    
    def logi_update(self):
        """
        Updates forces and controller connections, if the main window handler is found. This function needs to be 
        called every frame of your application.

        Args:
            None

        Returns:
            - bool: Returns True if successful, False if either:
                * LogiSteeringInitialize() hasn't been called, or
                * The main window handler could not be found.

        Example:
            >>> logi_update()
        """
        return self.LogiUpdate()
    
    def get_state_engines(self, index):
        """
        A simplified version of LogiGetState for use without DirectInput. Returns a DIJOYSTATE2ENGINES struct.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.

        Returns:
            - DIJOYSTATE2ENGINES: A structure containing the device's positional information for axes, POVs and buttons.

        Example:
            >>> get_state_engines(0)
        """
        return self.LogiGetStateENGINES(index)
    
    def get_device_path(self, index, buffer, buffer_size):
        """
        Retrieves the device's USB path for determining unique devices.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.
            - buffer (wchar_t*): A pre-allocated buffer that will hold the device path.
            - buffer_size (int): The size in bytes of the buffer.

        Returns:
            - bool: True if successful, False if there was an error copying the path into the buffer.

        Example:
            >>> get_device_path(0, buffer, buffer_size)
        """
        return self.LogiGetDevicePath(index, buffer, buffer_size)
    
    def get_friendly_product_name(self, index, buffer, buffer_size):
        """
        Retrieves the device's friendly product name.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.
            - buffer (wchar_t*): A pre-allocated buffer that will contain the device's friendly product name.
            - buffer_size (int): The size in bytes of the buffer.

        Returns:
            - bool: True if successful, False if there was an error copying the name into the buffer.

        Example:
            >>> get_friendly_product_name(0, buffer, buffer_size)
        """
        return self.LogiGetFriendlyProductName(index, buffer, buffer_size)
    
    def is_connected(self, index):
        """
        Checks if a game controller is connected at the specified index.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.

        Returns:
            - bool: True if a device is connected at the specified index, False otherwise.

        Example:
            >>> is_connected(0)
        """
        return self.LogiIsConnected(index)

    
    def is_device_connected(self, index, device_type):
        """
        Checks if the specified device is connected at the given index.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.
            - device_type (int): Type of the device to check for. Possible types are: 
                * LOGI_DEVICE_TYPE_WHEEL
                * LOGI_DEVICE_TYPE_JOYSTICK
                * LOGI_DEVICE_TYPE_GAMEPAD
                * LOGI_DEVICE_TYPE_OTHER

        Returns:
            - bool: True if the specified device is connected at that index, False otherwise.

        Example:
            >>> is_device_connected(0, LOGI_DEVICE_TYPE_WHEEL)
        """
        return self.LogiIsDeviceConnected(index, device_type)
    
    def is_manufacturer_connected(self, index, manufacturer_name):
        """
        Checks if the device connected at the given index is made by the specified manufacturer.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.
            - manufacturer_name (int): Name of the manufacturer the device has been made by. Possible types are: 
                * LOGI_MANUFACTURER_LOGITECH
                * LOGI_MANUFACTURER_MICROSOFT
                * LOGI_MANUFACTURER_OTHER

        Returns:
            - bool: True if a PC controller of the specified manufacturer is connected, False otherwise.

        Example:
            >>> is_manufacturer_connected(0, LOGI_MANUFACTURER_LOGITECH)
        """
        return self.LogiIsManufacturerConnected(index, manufacturer_name)

    def is_model_connected(self, index, model_name):
        """
        Checks if a controller of the specified model is connected at the given index.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.
            - model_name (int): Name of the model of the device. Possible types include various models such as: 
                * LOGI_MODEL_G27
                * LOGI_MODEL_G25
                * LOGI_MODEL_MOMO_RACING
                * LOGI_MODEL_MOMO_FORCE
                * LOGI_MODEL_DRIVING_FORCE_PRO
                * And many more...

        Returns:
            - bool: True if a controller of the specified model is connected, False otherwise.

        Example:
            >>> is_model_connected(0, LOGI_MODEL_G27)
        """
        return self.LogiIsModelConnected(index, model_name)

    def button_triggered(self, index, button_number):
        """
        Checks if the device connected at the given index is currently triggering the specified button.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.
            - button_number (int): The number of the button that we want to check. Possible numbers are: 0 to 127.

        Returns:
            - bool: True if the button was triggered, False otherwise.

        Example:
            >>> button_triggered(0, 1)
        """
        return self.LogiButtonTriggered(index, button_number)

    def button_released(self, index, button_number):
        """
        Checks if the specified button on the device connected at the given index has been released.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.
            - button_number (int): The number of the button that we want to check. Possible numbers are: 0 to 127.

        Returns:
            - bool: True if the button was released, False otherwise.

        Example:
            >>> button_released(0, 1)
        """
        return self.LogiButtonReleased(index, button_number)

    def button_is_pressed(self, index, button_number):
        """
        Checks if the specified button on the device connected at the given index is currently being pressed.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
            Index 1 to the second game controller.
            - button_number (int): The number of the button that we want to check. Possible numbers are: 0 to 127.

        Returns:
            - bool: True if the button is being pressed, False otherwise.

        Example:
            >>> button_is_pressed(0, 1)
        """
        return self.LogiButtonIsPressed(index, button_number)

    def generate_non_linear_values(self, index, non_lin_coeff):
        """
        Generates non-linear values for the game controller's axis to improve gameplay by reducing
        sensitivity issues. This method defines a non-linearity coefficient which determines how strongly
        non-linear the curve will be, creating a mapping table in the form of an array.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected. 
                        Index 1 to the second game controller.
            - non_lin_coeff (int): Value representing how much non-linearity should be applied. Range is -100 to 100. 
                                    0 = linear curve, 100 = maximum non-linear curve with less sensitivity around center,
                                    -100 = maximum non-linearity with more sensitivity around center position.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> generate_non_linear_values(0, 50)
        """
        return self.LogiGenerateNonLinearValues(index, non_lin_coeff)

    def get_non_linear_value(self, index, input_value):
        """
        Returns a non-linear value from a table previously generated using LogiGenerateNonLinearValues().
        This can be used for the response of a steering wheel.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected.
                        Index 1 to the second game controller.
            - input_value (int): Value between -32768 and 32767 corresponding to the original value of an axis.

        Returns:
            - int: Value between -32768 and 32767, corresponding to the level of non-linearity previously set with
                LogiGenerateNonLinearValues().

        Example:
            >>> get_non_linear_value(0, 16384)
        """
        return self.LogiGetNonLinearValue(index, input_value)

    def has_force_feedback(self, index):
        """
        Checks if the controller at the given index has force feedback capability.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected.
                        Index 1 to the second game controller.

        Returns:
            - bool: Returns True if the device can do force feedback, False otherwise.

        Example:
            >>> has_force_feedback(0)
        """
        return self.LogiHasForceFeedback(index)

    def is_playing(self, index, force_type):
        """
        Checks if a certain force effect is currently playing on the given game controller.

        Args:
            - index (int): Index of the game controller. Index 0 corresponds to the first game controller connected.
                        Index 1 to the second game controller.
            - force_type (int): The type of force that we want to check if it is playing. Possible types are:
                - LOGI_FORCE_SPRING
                - LOGI_FORCE_CONSTANT
                - LOGI_FORCE_DAMPER
                - LOGI_FORCE_SIDE_COLLISION
                - LOGI_FORCE_FRONTAL_COLLISION
                - LOGI_FORCE_DIRT_ROAD
                - LOGI_FORCE_BUMPY_ROAD
                - LOGI_FORCE_SLIPPERY_ROAD
                - LOGI_FORCE_SURFACE_EFFECT
                - LOGI_FORCE_CAR_AIRBORNE

        Returns:
            - bool: Returns True if the force is playing, False otherwise.

        Example:
            >>> is_playing(0, LOGI_FORCE_SPRING)
        """
        return self.LogiIsPlaying(index, force_type)

    def play_spring_force(self, index, offset_percentage, saturation_percentage, coefficient_percentage):
        """
        Plays the spring force.

        Args:
            - index (int): Index of the game controller.
            - offset_percentage (int): Center of the spring force effect (-100 to 100).
            - saturation_percentage (int): Saturation level of the spring force effect (0 to 100).
            - coefficient_percentage (int): Slope of effect strength increase (-100 to 100).

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_spring_force(0, 0, 50, 30)
        """
        return self.LogiPlaySpringForce(index, offset_percentage, saturation_percentage, coefficient_percentage)

    def stop_spring_force(self, index):
        """
        Stops the spring force.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> stop_spring_force(0)
        """
        return self.LogiStopSpringForce(index)

    def play_constant_force(self, index, magnitude_percentage):
        """
        Plays the constant force.

        Args:
            - index (int): Index of the game controller.
            - magnitude_percentage (int): Magnitude of the constant force effect (-100 to 100).

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_constant_force(0, 50)
        """
        return self.LogiPlayConstantForce(index, magnitude_percentage)

    def stop_constant_force(self, index):
        """
        Stops the constant force.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> stop_constant_force(0)
        """
        return self.LogiStopConstantForce(index)

    def play_damper_force(self, index, coefficient_percentage):
        """
        Plays the damper force.

        Args:
            - index (int): Index of the game controller.
            - coefficient_percentage (int): Slope of the effect strength increase relative to the amount of
                                            deflection from the center of the condition (-100 to 100).

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_damper_force(0, 50)
        """
        return self.LogiPlayDamperForce(index, coefficient_percentage)

    def stop_damper_force(self, index):
        """
        Stops the damper force.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> stop_damper_force(0)
        """
        return self.LogiStopDamperForce(index)

    def play_side_collision_force(self, index, magnitude_percentage):
        """
        Plays the side collision force.

        Args:
            - index (int): Index of the game controller.
            - magnitude_percentage (int): Specifies the magnitude of the side collision force effect (-100 to 100).

        Returns:
            - bool: Returns True if successful, False otherwise.

        Note:
            If you are already using a constant force tied to a vector force from the physics engine, side collisions 
            may be automatically taken care of by the constant force.

        Example:
            >>> play_side_collision_force(0, 50)
        """
        return self.LogiPlaySideCollisionForce(index, magnitude_percentage)

    def play_frontal_collision_force(self, index, magnitude_percentage):
        """
        Plays the frontal collision force.

        Args:
            - index (int): Index of the game controller.
            - magnitude_percentage (int): Specifies the magnitude of the frontal collision force effect (0 to 100).

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_frontal_collision_force(0, 50)
        """
        return self.LogiPlayFrontalCollisionForce(index, magnitude_percentage)

    def play_dirt_road_effect(self, index, magnitude_percentage):
        """
        Plays the dirt road effect.

        Args:
            - index (int): Index of the game controller.
            - magnitude_percentage (int): Specifies the magnitude of the dirt road effect (0 to 100).

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_dirt_road_effect(0, 50)
        """
        return self.LogiPlayDirtRoadEffect(index, magnitude_percentage)

    def stop_dirt_road_effect(self, index):
        """
        Stops the dirt road effect.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> stop_dirt_road_effect(0)
        """
        return self.LogiStopDirtRoadEffect(index)

    def play_bumpy_road_effect(self, index, magnitude_percentage):
        """
        Plays the bumpy road effect.

        Args:
            - index (int): Index of the game controller.
            - magnitude_percentage (int): Specifies the magnitude of the bumpy road effect (0 to 100).

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_bumpy_road_effect(0, 50)
        """
        return self.LogiPlayBumpyRoadEffect(index, magnitude_percentage)

    def stop_bumpy_road_effect(self, index):
        """
        Stops the bumpy road effect.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> stop_bumpy_road_effect(0)
        """
        return self.LogiStopBumpyRoadEffect(index)

    def play_slippery_road_effect(self, index, magnitude_percentage):
        """
        Plays the slippery road effect.

        Args:
            - index (int): Index of the game controller.
            - magnitude_percentage (int): Specifies the magnitude of the slippery road effect (0 to 100).
                                        100 corresponds to the most slippery effect.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_slippery_road_effect(0, 50)
        """
        return self.LogiPlaySlipperyRoadEffect(index, magnitude_percentage)

    def stop_slippery_road_effect(self, index):
        """
        Stops the slippery road effect.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> stop_slippery_road_effect(0)
        """
        return self.LogiStopSlipperyRoadEffect(index)

    def play_surface_effect(self, index, type, magnitude_percentage, period):
        """
        Plays the surface effect.

        Args:
            - index (int): Index of the game controller.
            - type (int): Specifies the type of force effect. Can be one of the following values:
                - LOGI_PERIODICTYPE_SINE
                - LOGI_PERIODICTYPE_SQUARE
                - LOGI_PERIODICTYPE_TRIANGLE
            - magnitude_percentage (int): Specifies the magnitude of the surface effect (0 to 100).
            - period (int): Specifies the period of the periodic force effect in milliseconds (20-150ms).

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_surface_effect(0, LOGI_PERIODICTYPE_SINE, 50, 120)
        """
        return self.LogiPlaySurfaceEffect(index, type, magnitude_percentage, period)

    def stop_surface_effect(self, index):
        """
        Stops the surface effect.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> stop_surface_effect(0)
        """
        return self.LogiStopSurfaceEffect(index)

    def play_car_airborne(self, index):
        """
        Plays the car airborne effect.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_car_airborne(0)
        """
        return self.LogiPlayCarAirborne(index)

    def stop_car_airborne(self, index):
        """
        Stops the car airborne road effect.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> stop_car_airborne(0)
        """
        return self.LogiStopCarAirborne(index)

    def play_softstop_force(self, index, usable_range_percentage):
        """
        Plays the soft stop force.

        Args:
            - index (int): Index of the game controller.
            - usable_range_percentage (int): Specifies the deadband in percentage of the softstop force effect.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_softstop_force(0, 50)
        """
        return self.LogiPlaySoftstopForce(index, usable_range_percentage)

    def stop_softstop_force(self, index):
        """
        Stops the soft stop force.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> stop_softstop_force(0)
        """
        return self.LogiStopSoftstopForce(index)

    def set_preferred_controller_properties(self, properties):
        """
        Sets preferred wheel properties.

        Args:
            - properties (LogiControllerPropertiesData): Structure containing all the fields to be set.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> set_preferred_controller_properties(properties)
        """
        return self.LogiSetPreferredControllerProperties(properties)

    def get_current_controller_properties(self, index, properties):
        """
        Fills the properties parameter with the current controller properties.

        Args:
            - index (int): Index of the game controller.
            - properties (LogiControllerPropertiesData): Structure to receive current properties.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> get_current_controller_properties(0, properties)
        """
        return self.LogiGetCurrentControllerProperties(index, properties)

    def get_shifter_mode(self, index):
        """
        Gets the current shifter mode (gated or sequential) for the game controller.

        Args:
            - index (int): Index of the game controller.

        Returns:
            - int: Returns 1 if the shifter is gated, 0 if the shifter is sequential, or -1 if unknown.

        Example:
            >>> get_shifter_mode(0)
        """
        return self.LogiGetShifterMode(index)

    def get_operating_range(self, index, range):
        """
        Retrieves the current operating range of the game controller.

        Args:
            - index (int): Index of the game controller.
            - range (int): Integer to receive the current operating range.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> get_operating_range(0, range)
        """
        return self.LogiGetOperatingRange(index, range)

    def set_operating_range(self, index, range):
        """
        Sets the operating range of the controller with the range parameter.

        Args:
            - index (int): Index of the game controller.
            - range (int): The operating range to be set.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> set_operating_range(0, 50)
        """
        return self.LogiSetOperatingRange(index, range)

    def play_leds(self, index, current_rpm, rpm_first_led_turns_on, rpm_red_line):
        """
        Plays the LEDs on the game controller.

        Args:
            - index (int): Index of the game controller.
            - current_rpm (float): Current RPM.
            - rpm_first_led_turns_on (float): RPM when first LEDs are to turn on.
            - rpm_red_line (float): Just below this RPM, all LEDs will be on. Just above, all LEDs will start flashing.

        Returns:
            - bool: Returns True if successful, False otherwise.

        Example:
            >>> play_leds(0, 5000, 6000, 7000)
        """
        return self.LogiPlayLeds(index, current_rpm, rpm_first_led_turns_on, rpm_red_line)

    def steering_shutdown(self):
        """
        Shuts down the SDK and destroys the controller objects. Also destroys the GUI window if it exists.

        Args:
            None

        Returns:
            None

        Example:
            >>> steering_shutdown()
        """
        # Destroy the GUI window if it exists
        if hasattr(self, 'root'):
            self.root.destroy()
        return self.LogiSteeringShutdown()
