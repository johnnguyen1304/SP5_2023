from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def getArea(self):
        return self.side * self.side

    def draw(self):
        for _ in range(self.side):
            print("#" * self.side)

# Example usage
square = Square(5)

print("Square Area:", square.getArea())
print("Drawing square:")
square.draw()
