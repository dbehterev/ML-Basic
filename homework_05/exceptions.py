"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    """Exception for low fuel"""
    
    def __init__(self, message):
        super().__init__(message)

class NotEnoughFuel(Exception):
    """Exception for not enough fuel"""
    
    def __init__(self, message):
        super().__init__(message)
    
class CargoOverload(Exception):
    """Exception for cargo overload"""
    
    def __init__(self, message):
        super().__init__(message)