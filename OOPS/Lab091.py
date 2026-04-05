#Method Overriding- Same name of method in parent and child class. Child always override the parent function.
#Super means call  my parent function, Note: Super can call only immediate parent function

import math


class Shape:
    def area(self):
        print("Area of Shape")

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        super().area()   #Super means call  my parent function
        return math.pi * self.radius * self.radius


shape1=Rectangle(10,20)
print(shape1.area())
shape2=Circle(5)
print(shape2.area())