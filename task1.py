class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle("red", 5)
print("Circle Area:", circle.area())

rectangle = Rectangle("blue", 4, 6)
print("Rectangle Area:", rectangle.area())