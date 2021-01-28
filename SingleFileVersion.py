# Python 3.9.1
# - when the registered class is in the same file.
#   - Can use class decorator method
#   - Similarly, __init_subclass__ acan be used too

from abc import ABC, abstractmethod

class CarRegistry():

    __cars = {}

    @classmethod
    def register(cls, car_type:str):
        def decorator(subclass):
            if issubclass(subclass,Car):
                cls.__cars[car_type] = subclass
            return subclass
        return decorator

    @classmethod
    def create(cls, car_type:str):
        if car_type not in cls.__cars:
            raise ValueError('Car type %s is not registered' % car_type)
        return cls.__cars[car_type]()

class Car(ABC):
    
    @abstractmethod
    def drive(self):
        pass

@CarRegistry.register('Holden')
class Holden(Car):

    def drive(self):
        print('I\'m driving Holden!')


@CarRegistry.register('Ford')
class Ford(Car):

    def drive(self):
        print('I\'m driving Ford!')    

if __name__ == '__main__':
    car = CarRegistry.create('Holden')
    car.drive()

    car = CarRegistry.create('Ford')
    car.drive()