from .constants import LogitechControllerConstants
from .structs import LogitechControllerStructs
from .functions import LogitechControllerFunctions


class LogitechController(LogitechControllerConstants, LogitechControllerStructs, LogitechControllerFunctions):
    def __init__(self, dll_path):
        self.structs = LogitechControllerStructs()
        LogitechControllerFunctions.__init__(self, dll_path, self.structs)
