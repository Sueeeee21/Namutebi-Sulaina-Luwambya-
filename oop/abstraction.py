from abc import ABC, abstractmethod

from math import pi

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass

#     @abstractmethod
#     def stop_engine(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started.")

#     def stop_engine(self):
#         print("Car engine stopped.")

# car = Car()
# car.start_engine()  
# car.stop_engine()

class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shapes):   
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

rect = Rectangle(5, 3)
print("Rectangle:")
print(f"  Area      : {rect.area()}")
print(f"  Perimeter : {rect.perimeter()}")

circle = Circle(7)
print("\nCircle:")
print(f"  Area      : {circle.area():.2f}")
print(f"  Perimeter : {circle.perimeter():.2f}")

