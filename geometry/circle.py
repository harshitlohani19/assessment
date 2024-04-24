import math

class Circle:
    """
    A class to represent a circle.

    Attributes:
    - radius (float): The radius of the circle.

    Methods:
    - area(): Compute the area of the circle.
    - circumference(): Compute the circumference of the circle.
    - __str__(): Return a string representation of the circle.
    - __eq__(other): Compare this circle with another circle based on their areas.
    - __lt__(other): Compare this circle with another circle based on their areas.
    """

    def __init__(self, radius):
        """
        Initialize a Circle object with the given radius.

        Parameters:
        - radius (float): The radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """
        Compute the area of the circle.

        Returns:
        - float: The area of the circle.
        """
        return math.pi * self.radius ** 2
    
    def circumference(self):
        """
        Compute the circumference of the circle.

        Returns:
        - float: The circumference of the circle.
        """
        return 2 * math.pi * self.radius
    
    def __str__(self):
        """
        Return a string representation of the circle.

        Returns:
        - str: String representation of the circle.
        """
        return f"Circle with radius {self.radius}, Area: {self.area()}, Circumference: {self.circumference()}"
    
    def __eq__(self, other):
        """
        Compare this circle with another circle based on their areas.

        Parameters:
        - other (Circle): Another circle object to compare with.

        Returns:
        - bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()
    
    def __lt__(self, other):
        """
        Compare this circle with another circle based on their areas.

        Parameters:
        - other (Circle): Another circle object to compare with.

        Returns:
        - bool: True if the area of this circle is less than the area of the other circle, False otherwise.
        """
        return self.area() < other.area()
