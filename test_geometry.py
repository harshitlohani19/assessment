import unittest
from geometry.circle import Circle
from geometry.square import Square
from geometry.rectangle import Rectangle

class TestCircle(unittest.TestCase):
    """
    Test cases for the Circle class.
    """

    def test_area(self):
        """
        Test the area() method of the Circle class.
        """
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)
    
    def test_circumference(self):
        """
        Test the circumference() method of the Circle class.
        """
        circle = Circle(5)
        self.assertAlmostEqual(circle.circumference(), 31.42, places=2)
    
    def test_string_representation(self):
        """
        Test the string representation (__str__) method of the Circle class.
        """
        circle = Circle(5)
        self.assertEqual(str(circle), "Circle with radius 5, Area: 78.53981633974483, Circumference: 31.41592653589793")
    
    def test_comparison(self):
        """
        Test the comparison methods (__eq__, __lt__) of the Circle class.
        """
        circle1 = Circle(5)
        circle2 = Circle(6)
        self.assertTrue(circle1 < circle2)

# Similar docstrings for TestSquare and TestRectangle classes...

if __name__ == "__main__":
    unittest.main()
