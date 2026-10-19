# Name: Janvi
# Roll Number: 26570025

# Practical 14: Inherit the above class to create a "3DPoint" with an additional attribute z.
# Override the method defined in "2DPoint" to calculate the distance between two points of the
# "3DPoint" class.
# Note: class names cannot start with a digit, so the classes are Point2D and Point3D.
# Keep practical_13_point2d.py in the same folder as this file.
import math
from practical_13_point2d import Point2D


class Point3D(Point2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)                  # x and y are set by the parent class
        self.z = z

    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"

    def distance(self, other):
        """Overridden: distance in 3-D space."""
        return math.sqrt((self.x - other.x) ** 2 +
                         (self.y - other.y) ** 2 +
                         (self.z - getattr(other, "z", 0)) ** 2)

    def move(self, dx, dy, dz):
        """Overridden: shift the point by (dx, dy, dz)."""
        super().move(dx, dy)
        self.z += dz


if __name__ == "__main__":
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(4, 6, 15)
    print("p1 =", p1)
    print("p2 =", p2)
    print("Distance between p1 and p2 =", p1.distance(p2))

    p1.move(1, 1, 1)
    print("After moving p1 by (1, 1, 1): p1 =", p1)

    # The parent class is still available and unchanged
    q1, q2 = Point2D(0, 0), Point2D(3, 4)
    print("2D distance:", q1.distance(q2))
    print("Point3D is a Point2D:", isinstance(p1, Point2D))

    # Points entered by the user
    x1, y1, z1 = map(float, input("\nEnter x, y and z of the first point: ").split())
    x2, y2, z2 = map(float, input("Enter x, y and z of the second point: ").split())
    a, b = Point3D(x1, y1, z1), Point3D(x2, y2, z2)
    print(a, "and", b)
    print("Distance =", round(a.distance(b), 4))
