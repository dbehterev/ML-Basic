"""
класс `Car`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
    
    def __init__(self, weight: float = 1000, fuel: float = 40, fuel_consumption: float = 10):
        """Initialization attributes of the class"""
        
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine):
        if not isinstance(engine, Engine):
            raise ValueError("engine should be instance of Engine class")

        self.engine = engine
        
#eng1 = Engine(3.5, 8)

#my_car = Car(1.5)
#my_car.set_engine(eng1)
#print(my_car.engine)
