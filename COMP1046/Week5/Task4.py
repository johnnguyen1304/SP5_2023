#Task1
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



#Task 2-4
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Square(Shape):
    def __init__(self, width):
        self.__width = width

    def getArea(self):
        return self.__width * self.__width

    def draw(self):
        for _ in range(self.__width):
            print("#" * self.__width)

class Triangle(Shape):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def getArea(self):
        return 0.5 * self.__base * self.__height

    def draw(self):
        for i in range(1, self.__height + 1):
            print("*" * int((i / self.__height) * self.__base))

# Test cases
shapes = [Square(4), Triangle(7, 5)]
for shape in shapes:
    print(f'This {type(shape).__name__} has an area of {shape.getArea()}')
    shape.draw()
    print()

# Additional test case
shape = Shape()  
# This line will result in an error, since you cannot create an instance of an abstract class.


