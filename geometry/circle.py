import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle with radius {self.radius}, Area: {self.area()}, Circumference: {self.circumference()}"
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()
