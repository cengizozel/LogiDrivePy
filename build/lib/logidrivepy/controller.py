from .constants import LogitechControllerConstants
from .structs import LogitechControllerStructs
from .functions import LogitechControllerFunctions
import pathlib

class LogitechController(LogitechControllerConstants, LogitechControllerStructs, LogitechControllerFunctions):
    def __init__(self, dll_path=None):
        if dll_path is None:
            # Get the location of the current file (controller.py)
            current_file_path = pathlib.Path(__file__)
            # Get the absolute path to the DLL
            dll_path = current_file_path.parent / 'dll' / 'LogitechSteeringWheelEnginesWrapper.dll'

        self.structs = LogitechControllerStructs()
        LogitechControllerFunctions.__init__(self, str(dll_path), self.structs)
