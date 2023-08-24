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

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def getArea(self):
        return 0.5 * self.base * self.height

    def draw(self):
        for i in range(1, self.height + 1):
            print("*" * int((i / self.height) * self.base))

# Test cases
shapes = [Square(4), Triangle(7, 5)]
for shape in shapes:
    print(f'This {type(shape).__name__} has an area of {shape.getArea()}')
    shape.draw()
    print()

# Additional test case
shape = Shape()  
# This line will result in an error, since you cannot create an instance of an abstract class.


