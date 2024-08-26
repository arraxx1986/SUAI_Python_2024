class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def square(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width + self.height)

rect_1 = Rectangle(15,20)
assert rect_1.square() == 300
assert rect_1.perimeter() == 70

rect_2 = Rectangle(50,50)
assert rect_2.square() == 2500
assert rect_2.perimeter() == 200

print('Good')