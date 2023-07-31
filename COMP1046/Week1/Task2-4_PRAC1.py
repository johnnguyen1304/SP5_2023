from math import pi

def numberofCircles(length,width,radius):
    numberofCircles = areaofRectangle(length,width) / areaofCircle(radius)
    print('Number of Circles in Rectangle is',numberofCircles)
    return numberofCircles
def areaofRectangle(length,width):
    areaofRectangle = length * width
    print('Area of Rectangle is', areaofRectangle)
    return areaofRectangle
def areaofCircle(radius):
    areaofCircle = pow(radius,2) * pi
    print('Area of Circle is', areaofCircle)
    return areaofCircle
    
numberofCircles(10,5,5)