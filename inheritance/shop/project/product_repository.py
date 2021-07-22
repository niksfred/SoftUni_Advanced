from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for object in self.products:
            if object.name == product_name:
                return object

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        res = [f"{product.name}: {product.quantity}" for product in self.products]
        return "\n".join(res)
