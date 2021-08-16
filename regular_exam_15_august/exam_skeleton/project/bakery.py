from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str) -> None:
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))


    def add_drink(self, drink_type: str, name: str, portion: int, brand:str):
        for d in self.drinks_menu:
            if d.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == "Water":
            self.drinks_menu.append(Water(name, portion, brand))
            

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for t in self.tables_repository:
            if t.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))


    def reserve_table(self, number_of_people: int):
        for t in self.tables_repository:
            if not t.is_reserved and number_of_people <= t.capacity:
                t.reserve(number_of_people)
                return f"Table {t.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    # def order_food(self, table_number: int, *args):
    #     ordered_food = []
    #     for t in self.tables_repository:
    #         if t.table_number == table_number:
    #             for food in self.food_menu:
    #                 if food.name in args:
    #                     t.food_orders(food)
    #                     ordered_food.append(food.name)

    #             not_ordered = [f for f in args if f not in ordered_food]
    #             res = ""
    #             res += f"Table {table_number} ordered:\n"
    #             res += "\n".join(t.food_orders)
    #             res += f"{self.name} does not have in the menu:\n"
    #             res += "\n".join(not_ordered)
    #             return res

    #     return f"Could not find table {table_number}"
                

    # def order_drink(self, table_number: int, *args):
    #     ordered_drinks = []
    #     for t in self.tables_repository:
    #         if t.table_number == table_number:
    #             for drink in self.drinks_menu_menu:
    #                 if drink.name in args:
    #                     t.drink_orders(drink)
    #                     ordered_drinks.append(drink.name)

    #             not_ordered = [f for f in args if f not in ordered_drinks]
    #             res = ""
    #             res += f"Table {table_number} ordered:\n"
    #             res += "\n".join(t.drink_orders)
    #             res += f"{self.name} does not have in the menu:\n"
    #             res += "\n".join(not_ordered)
    #             return res

    #     return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        for t in self.tables_repository:
            if t.table_number == table_number:
                bill = t.get_bill()
                self.total_income += bill
                res = f"Table: {table_number}\nBill: {bill}"
                return res

    def get_free_tables_info(self):
        res = ""
        for t in self.tables_repository:
            if not t.is_reserved:
                res += f"{t}\n"
        return res


    def get_total_income(self):
        return self.total_income