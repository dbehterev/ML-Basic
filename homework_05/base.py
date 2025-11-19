"""
класс `Vehicle`
"""

from abc import ABC
from homework_05.exceptions import LowFuelError,NotEnoughFuel


class Vehicle(ABC):
    """Base class for vehicle"""
    
    def __init__(self, weight: float = 1000, fuel: float = 40, fuel_consumption: float = 10):
        """Initialization attributes of the class"""
        
        if weight <= 0:
            raise ValueError("Weight can't be zero or negative")
        elif fuel <= 0:
            raise ValueError("Fuel can't be zero or negative") 
        elif fuel_consumption <= 0:
            raise ValueError("Fuel consumption can't be zero or negative") 
        
        self.weight             = weight            # in kg
        self.fuel               = fuel              # 
        self.fuel_consumption   = fuel_consumption  # fuel consumption for every 100km
        self.started            = False
        
    def start(self) -> None:
        """Start engine"""
        
        if not self.started:
            if self.fuel == 0:
                raise LowFuelError("Too low fuel")
            self.started = True
        else:
            print("Already started!")
    
    def move(self, distance: float) -> None:
        """Moving vehicle
            distance in km
        """        
        
        if not self.started:
            print("Vehicle should be started before moving")
            return
        
        if distance <= 0:
            print("Distance should be positive")
            return
        
        if self.fuel == 0:
            raise LowFuelError("Too low fuel")
        
        fuel_need = (distance * self.fuel_consumption) / 100   
        if self.fuel < fuel_need:
            raise NotEnoughFuel("Shortage fuel by "+str(fuel_need - self.fuel))
        
        self.fuel -= fuel_need
        
        print(f"Rest of fuel {self.fuel}")
        