PI = 3.1415926


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * PI

    def compare(circle1, circle2):
        if circle1.area() != circle2.area():
            return 'Not equal'
        else:
            return 'Equal'


if __name__ == '__main__':
    c1 = Circle(2)
    c2 = Circle(3)
    print(c1.area())
    print(Circle.compare(c1, c2))


