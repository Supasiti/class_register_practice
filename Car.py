from abc import ABC, abstractmethod

class Car(ABC):
    
    @abstractmethod
    def drive(self):
        pass
