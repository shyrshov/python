# Create a Python class called "Car" with the following fields and methods:

# Fields:
# make (string)
# model (string)
# year (integer)
# speed (float)

# Methods:
# accelerate(): Increases the speed of the car by 10 units.
# brake(): Decreases the speed of the car by 10 units.
# get_speed(): Returns the current speed of the car.

class Car:
    def __init__(self, make: str, model: str, year: int, speed: float):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
    
    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed
    
car = Car("Toyota", "Auris", 2005, 140)
print(car.get_speed())
car.accelerate()
car.accelerate()
print(car.get_speed())
car.brake()
print(car.get_speed())