class Product:
    count = 0
    totalPrice = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
        Product.totalPrice += price

    @classmethod
    def averagePrice(cls):
        if cls.count == 0:
            return 0.0
        return cls.totalPrice / cls.count

# Test cases
Product("Pen", 3.0)
Product("Notebook", 5.0)
Product("Eraser", 1.5)
Product("Pencil", 2.5)

print("Average product price:", Product.averagePrice())
