from math import pi

class Rectangle:
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def areaOfCircle(self):
        return pi * pow(self.radius,2) 

    def numberOfCircles(self):
        return self.length * self.width / (pi * pow(self.radius,2))  


Rectangle = Rectangle(length=100, width=50, radius=10)


area_of_circle = Rectangle.areaOfCircle()
num_of_circles = Rectangle.numberOfCircles()


print("Area of the circle:", area_of_circle)
print("Number of circles that can fit in the rectangle:", num_of_circles)

    

  

