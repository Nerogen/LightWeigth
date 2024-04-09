from geometry import GeometryCalculator
import math
import unittest


class TestGeometryCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(GeometryCalculator.circle_area(1), math.pi)

    def test_triangle_area(self):
        self.assertAlmostEqual(GeometryCalculator.triangle_area(3, 4, 5), 6)

    def test_is_right_triangle(self):
        self.assertTrue(GeometryCalculator.is_right_triangle(3, 4, 5))
        self.assertFalse(GeometryCalculator.is_right_triangle(3, 4, 6))


if __name__ == "__main__":
    unittest.main()
