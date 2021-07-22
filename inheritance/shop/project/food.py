from project.product import Product

class Food(Product):

    def __init__(self, name) -> None:
        super().__init__(name, quantity=15)
    