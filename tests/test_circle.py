import unittest
import calculate


class TestCircle(unittest.TestCase):
    """Area tests."""

    def test_area_zero(self):
        res_area_zero = calculate.calc("circle", "area", [0])
        self.assertEqual(res_area_zero, 0)

    def test_area_positive(self):
        self.assertEqual(calculate.calc("circle", "area", [1]),
                         3.141592653589793)
        self.assertEqual(calculate.calc("circle", "area", [3]),
                         28.274333882308138)

    def test_area_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-1])
        self.assertEqual(str(context.exception), "Radius must be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-6])
        self.assertEqual(str(context.exception), "Radius must be > 0.")

    """Perimeter tests."""

    def test_perimeter_zero(self):
        res_perimeter_zero = calculate.calc("circle", "perimeter", [0])
        self.assertEqual(res_perimeter_zero, 0)

    def test_perimeter_positive(self):
        self.assertEqual(calculate.calc("circle", "perimeter", [1]),
                         6.283185307179586)
        self.assertEqual(calculate.calc("circle", "perimeter", [6]),
                         37.699111843077516)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-1])
        self.assertEqual(str(context.exception), "Radius must be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-6])
        self.assertEqual(str(context.exception), "Radius must be > 0.")


if __name__ == "__main__":
    unittest.main()
