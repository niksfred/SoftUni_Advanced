from project.topping import Topping
from project.dough import Dough


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int) -> None:
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        if dough == None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = dough
    
    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, toppings_capacity):
        if toppings_capacity <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = toppings_capacity

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if not topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight
    
    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())
