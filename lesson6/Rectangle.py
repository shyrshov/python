# Create a Python class called "Rectangle" with the following fields and methods:
# Field:
# length (float)
# width (float)
# Methods:
# calculate_area(): Calculates and returns the area of the rectangle.
# calculate_perimeter(): Calculates and returns the perimeter of the rectangle.

class Rectangle:

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return (self.length + self.width) * 2

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())