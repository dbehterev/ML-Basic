"""
класс `Plane`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    
    def __init__(self, max_cargo: float = 5000, fuel: float = 40, fuel_consumption: float = 10):
        """Initialization attributes of the class"""
        
        super().__init__(max_cargo, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo
            
    def load_cargo(self, cargo: float):
        if (cargo + self.cargo) > self.max_cargo:
            raise CargoOverload('Overweight by '+str((cargo + self.cargo) - self.max_cargo))
        
        self.cargo += cargo
        
    def remove_all_cargo(self):
        _cargo = self.cargo
        self.cargo = 0
        return _cargo

#my_plane = Plane(5000, 900, 150)
#my_plane.load_cargo(1000)
#my_plane.load_cargo(4000)
#my_plane.load_cargo(500)
#print(my_plane.remove_all_cargo())
#print(my_plane.cargo)