# Name: Janvi
# Roll Number: 26570025

# Practical 13: Define a class "2DPoint" with coordinates x and y as attributes. Create relevant
# methods and print the objects. Also define a method distance to calculate the distance between
# any two point objects.
# Note: a Python class name cannot start with a digit, so the class is called Point2D.
import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point2D({self.x}, {self.y})"

    def distance(self, other):
        """Distance between this point and another point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def move(self, dx, dy):
        """Shift the point by (dx, dy)."""
        self.x += dx
        self.y += dy

    def midpoint(self, other):
        return Point2D((self.x + other.x) / 2, (self.y + other.y) / 2)


if __name__ == "__main__":
    p1 = Point2D(1, 2)
    p2 = Point2D(4, 6)
    print("p1 =", p1)
    print("p2 =", p2)
    print("Distance between p1 and p2 =", p1.distance(p2))
    print("Midpoint of p1 and p2 =", p1.midpoint(p2))

    p1.move(2, 3)
    print("After moving p1 by (2, 3): p1 =", p1)

    # Points entered by the user
    x1, y1 = map(float, input("\nEnter x and y of the first point: ").split())
    x2, y2 = map(float, input("Enter x and y of the second point: ").split())
    a, b = Point2D(x1, y1), Point2D(x2, y2)
    print(a, "and", b)
    print("Distance =", round(a.distance(b), 4))
