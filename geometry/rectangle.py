class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    - width (float): The width of the rectangle.
    - height (float): The height of the rectangle.

    Methods:
    - area(): Compute the area of the rectangle.
    - perimeter(): Compute the perimeter of the rectangle.
    - __str__(): Return a string representation of the rectangle.
    - __eq__(other): Compare this rectangle with another rectangle based on their areas.
    - __lt__(other): Compare this rectangle with another rectangle based on their areas.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle object with the given width and height.

        Parameters:
        - width (float): The width of the rectangle.
        - height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height
    
    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
        - float: The area of the rectangle.
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Compute the perimeter of the rectangle.

        Returns:
        - float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        - str: String representation of the rectangle.
        """
        return f"Rectangle with width {self.width} and height {self.height}, Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __eq__(self, other):
        """
        Compare this rectangle with another rectangle based on their areas.

        Parameters:
        - other (Rectangle): Another rectangle object to compare with.

        Returns:
        - bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()
    
    def __lt__(self, other):
        """
        Compare this rectangle with another rectangle based on their areas.

        Parameters:
        - other (Rectangle): Another rectangle object to compare with.

        Returns:
        - bool: True if the area of this rectangle is less than the area of the other rectangle, False otherwise.
        """
        return self.area() < other.area()
