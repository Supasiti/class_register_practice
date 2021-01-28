# Python 3.9.1
# - when the registered class is in a different file.
#   - Cannot use class decorator method. It won't be called.
#   - Similarly, __init_subclass__ also is not called too.
#   - It is best to use factory pattern.

from Holden import Holden
from Ford import Ford

class CarRegistry():
    
    __cars = {
        'Holden': Holden, 
        'Ford' : Ford
    }

    # @classmethod
    # def register(cls, car_type: str):
    #     def decorator(subclass):
    #         if issubclass(subclass, Car):
    #             cls.__cars[car_type] = subclass
    #         return subclass
    #     return decorator
    
    @classmethod
    def create_car(cls, car_type: str):
        if car_type not in cls.__cars:
            raise ValueError('The following car type does not exist: %s ' % car_type)

        return cls.__cars[car_type]()