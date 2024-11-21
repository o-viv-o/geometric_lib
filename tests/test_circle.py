import unittest
import calculate

class TestCircle(unittest.TestCase):
    """Area tests."""

    def test_area_zero(self):
        res_area_zero = (calculate.calc("circle", "area", [0]), 0)

    def test_area_positive(self):
        self.assertEqual(calculate.calc("circle", "area", [1]), 3.14159)
        self.assertEqual(calculate.calc("circle", "area", [3]), 28.2743)

    def test_area_negative(self):
        error_message = "Radius must be > 0."
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-1])
        self.assertEqual(str(context.exception), error_message)

        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-6])
        self.assertEqual(str(context.exception), error_message)

    """Perimeter tests."""

    def test_perimeter_zero(self):
        res_perimeter_zero = calculate.calc("circle", "perimeter", [0])
        self.assertEqual(res_perimeter_zero, 0)

    def test_perimeter_positive(self):
        self.assertEqual(calculate.calc("circle", "perimeter", [1]), 6.283185307179586)
        self.assertEqual(calculate.calc("circle", "perimeter", [6]), 37.699111843077516)

    def test_perimeter_negative(self):
        error_message = "Radius must be > 0."
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-1])
        self.assertEqual(str(context.exception), error_message)

        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-6])
        self.assertEqual(str(context.exception), error_message)


if __name__ == "__main__":
    unittest.main()
