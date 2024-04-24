import sys
from geometry.circle import Circle
from geometry.square import Square
from geometry.rectangle import Rectangle

def main():
    """
    Main function to demonstrate the usage of the geometry module.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <figure_type> <dimensions>")
        sys.exit(1)
    
    figure_type = sys.argv[1]
    if figure_type == 'circle':
        if len(sys.argv) != 3:
            print("Usage: python main.py circle <radius>")
            sys.exit(1)
        radius = float(sys.argv[2])
        circle = Circle(radius)
        print(circle)
    
    elif figure_type == 'square':
        if len(sys.argv) != 3:
            print("Usage: python main.py square <side_length>")
            sys.exit(1)
        side_length = float(sys.argv[2])
        square = Square(side_length)
        print(square)
    
    elif figure_type == 'rectangle':
        if len(sys.argv) != 4:
            print("Usage: python main.py rectangle <width> <height>")
            sys.exit(1)
        width = float(sys.argv[2])
        height = float(sys.argv[3])
        rectangle = Rectangle(width, height)
        print(rectangle)
    
    else:
        print("Invalid figure type. Choose from 'circle', 'square', or 'rectangle'.")

if __name__ == "__main__":
    main()
