class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}, Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()
