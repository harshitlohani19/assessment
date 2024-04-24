class Square:
    """
    A class to represent a square.

    Attributes:
    - side_length (float): The side length of the square.

    Methods:
    - area(): Compute the area of the square.
    - perimeter(): Compute the perimeter of the square.
    - __str__(): Return a string representation of the square.
    - __eq__(other): Compare this square with another square based on their areas.
    - __lt__(other): Compare this square with another square based on their areas.
    """

    def __init__(self, side_length):
        """
        Initialize a Square object with the given side length.

        Parameters:
        - side_length (float): The side length of the square.
        """
        self.side_length = side_length
    
    def area(self):
        """
        Compute the area of the square.

        Returns:
        - float: The area of the square.
        """
        return self.side_length ** 2
    
    def perimeter(self):
        """
        Compute the perimeter of the square.

        Returns:
        - float: The perimeter of the square.
        """
        return 4 * self.side_length
    
    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        - str: String representation of the square.
        """
        return f"Square with side length {self.side_length}, Area: {self.area()}, Perimeter: {self.perimeter()}"
    
    def __eq__(self, other):
        """
        Compare this square with another square based on their areas.

        Parameters:
        - other (Square): Another square object to compare with.

        Returns:
        - bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()
    
    def __lt__(self, other):
        """
        Compare this square with another square based on their areas.

        Parameters:
        - other (Square): Another square object to compare with.

        Returns:
        - bool: True if the area of this square is less than the area of the other square, False otherwise.
        """
        return self.area() < other.area()
