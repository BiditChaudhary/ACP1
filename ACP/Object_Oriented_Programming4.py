class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
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

rectangle = Rectangle(10, 5)
print(f"A {rectangle.name} with length {rectangle.length} and width {rectangle.width} has:")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

square = Square(4)
print(f"\nA {square.name} with side length {square.length} has:")
print(f"Area: {square.area()}")
print(f"Perimeter: {square.perimeter()}")

