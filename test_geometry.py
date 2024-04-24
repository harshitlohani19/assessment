import unittest
from geometry.circle import Circle
from geometry.square import Square
from geometry.rectangle import Rectangle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)
    
    def test_circumference(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.circumference(), 31.42, places=2)
    
    def test_string_representation(self):
        circle = Circle(5)
        self.assertEqual(str(circle), "Circle with radius 5, Area: 78.53981633974483, Circumference: 31.41592653589793")
    
    def test_comparison(self):
        circle1 = Circle(5)
        circle2 = Circle(6)
        self.assertTrue(circle1 < circle2)

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)
    
    def test_perimeter(self):
        square = Square(4)
        self.assertEqual(square.perimeter(), 16)
    
    def test_string_representation(self):
        square = Square(4)
        self.assertEqual(str(square), "Square with side length 4, Area: 16, Perimeter: 16")
    
    def test_comparison(self):
        square1 = Square(4)
        square2 = Square(5)
        self.assertTrue(square1 < square2)

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)
    
    def test_perimeter(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.perimeter(), 14)
    
    def test_string_representation(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(str(rectangle), "Rectangle with width 3 and height 4, Area: 12, Perimeter: 14")
    
    def test_comparison(self):
        rectangle1 = Rectangle(3, 4)
        rectangle2 = Rectangle(4, 5)
        self.assertTrue(rectangle1 < rectangle2)

if __name__ == "__main__":
    unittest.main()
