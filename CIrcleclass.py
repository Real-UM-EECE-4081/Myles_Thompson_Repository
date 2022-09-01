import math
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return 2 * self.radius * math.pi

NewCircle = Circle(30)
print('%.2f' % NewCircle.area())
print('%.2f' % NewCircle.perimeter())