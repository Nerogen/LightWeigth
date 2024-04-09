import math


class GeometryCalculator:
    @staticmethod
    def circle_area(radius: float) -> float:
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1: float, side2: float, side3: float) -> float:
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    @staticmethod
    def is_right_triangle(side1: float, side2: float, side3: float) -> float:
        sides = [side1, side2, side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


