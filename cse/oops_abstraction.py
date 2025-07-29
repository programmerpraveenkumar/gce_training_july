from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# shape_obj = Shape() # This would raise a TypeError as Shape is abstract
circle = Circle(5)
print(f"Circle Area: {circle.area()}")