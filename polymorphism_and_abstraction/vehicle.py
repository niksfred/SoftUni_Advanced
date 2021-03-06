from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        self.fuel_quantity =  fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        air_conditioner = 0.9
        fuel_needed = (self.fuel_consumption + air_conditioner) * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        self.fuel_quantity =  fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        air_conditioner = 1.6
        fuel_needed = (self.fuel_consumption + air_conditioner) * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        loses = 0.95
        self.fuel_quantity += fuel * loses

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
