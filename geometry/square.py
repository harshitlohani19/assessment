class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    
    def perimeter(self):
        return 4 * self.side_length
    
    def __str__(self):
        return f"Square with side length {self.side_length}, Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()
