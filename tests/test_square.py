import unittest
import calculate

from square import area, perimeter


class TestSquare(unittest.TestCase):
    """Area tests."""

    def test_area_zero(self):
        res_area_zero = calculate.calc("square", "area", [0])
        self.assertEqual(res_area_zero, 0)

    def test_area_positive(self):
        res_area_1_pos = calculate.calc("square", "area", [1])
        self.assertEqual(res_area_1_pos, 1)

        res_area_2_pos = calculate.calc("square", "area", [6])
        self.assertEqual(res_area_2_pos, 36)

    def test_area_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "area", [-1])
        self.assertEqual(str(context.exception), "Size must be greater than zero.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "area", [-6])
        self.assertEqual(str(context.exception), "Size must be greater than zero.")

    """Perimeter tests."""

    def test_perimeter_zero(self):
        res_perimeter_zero = calculate.calc("square", "perimeter", [0])
        self.assertEqual(res_perimeter_zero, 0)

    def test_perimeter_positive(self):
        res_perimeter_1_pos = calculate.calc("square", "perimeter", [1])
        self.assertEqual(res_perimeter_1_pos, 4)

        res_perimeter_2_pos = calculate.calc("square", "perimeter", [6])
        self.assertEqual(res_perimeter_2_pos, 24)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "perimeter", [-1])
        self.assertEqual(str(context.exception), "Size must be greater than zero.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "perimeter", [-6])
        self.assertEqual(str(context.exception), "Size must be greater than zero.")


if __name__ == "__main__":
    unittest.main()
