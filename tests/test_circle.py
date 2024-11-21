import unittest
import calculate
import math
from circle import area, perimeter


class TestCircle(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(5), math.pi * 25, places=5)

    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5, places=5)

   def test_area_negative(self):
        error_message = "Radius must be > 0."
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-1])
        self.assertEqual(str(context.exception), error_message)

        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-6])
        self.assertEqual(str(context.exception), error_message)
       
   def test_perimeter_negative(self):
        error_message = "Radius must be > 0."
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-1])
        self.assertEqual(str(context.exception), error_message)

        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-6])
        self.assertEqual(str(context.exception), error_message)
   


if __name__ == '__main__':
    unittest.main()
