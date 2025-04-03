# Parent class for general geometrical shapes
class Shape:
    def __init__(self, name):
        self.name = name
    
    # Method to display the name of the shape
    def display(self):
        print(f"This is a {self.name}.")

# Child class for Rectangle, inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        # Initializing the parent class constructor
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    

    def area(self):
        return self.length * self.width
  
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.name = "Square" 

shape = Shape("Generic Shape")
rectangle = Rectangle(5, 3)
square = Square(4)

shape.display()
print(f"Area of Rectangle: {rectangle.area()} sq.units")
print(f"Perimeter of Rectangle: {rectangle.perimeter()} units")

square.display()
print(f"Area of Square: {square.area()} sq.units")
print(f"Perimeter of Square: {square.perimeter()} units")
