class PizzaDelivery:

    ordered = False

    def __init__(self, name, price:float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if not PizzaDelivery.ordered:
            if not ingredient in self.ingredients.keys():
                self.ingredients[ingredient] = 0
            self.ingredients[ingredient] += quantity
            self.price += quantity * price_per_ingredient
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if not PizzaDelivery.ordered:

            if ingredient in self.ingredients.keys():
                if quantity > self.ingredients[ingredient]:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.ingredients[ingredient] -= quantity
                    self.price -= quantity * price_per_ingredient
            else:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"


    def make_order(self):
        PizzaDelivery.ordered = True
        key_value = [f"{key}: {value}" for key, value in self.ingredients.items()]
        res = ""
        res += f"You've ordered pizza {self.name} prepared with "
        res += ", ".join(key_value)
        res += f" and the price will be {self.price}lv."
        return res

margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))