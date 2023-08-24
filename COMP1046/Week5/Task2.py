from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def getArea(self):
        return self.side * self.side

    def draw(self):
        print(f"Drawing a square with side {self.side}")

# Example usage
circle = Circle(5)
square = Square(4)

print("Circle Area:", circle.getArea())
circle.draw()

print("Square Area:", square.getArea())
square.draw()
