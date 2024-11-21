import unittest
import calculate


class TestTriangle(unittest.TestCase):
    """Area tests."""

    def test_area_zero(self):
        res_area_zero = calculate.calc("triangle", "area", [0, 0, 0])
        self.assertEqual(res_area_zero, 0)

    def test_area_positive(self):
        res_area_1_pos = calculate.calc("triangle", "area", [1, 1, 1])
        self.assertEqual(res_area_1_pos, 1.5)

        res_area_2_pos = calculate.calc("triangle", "area", [6, 6, 6])
        self.assertEqual(res_area_2_pos, 9)

    def test_area_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "area", [-1, -1, -1])
        self.assertEqual(str(context.exception),
                         "Size must be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "area", [-6, -6, -6])
        self.assertEqual(str(context.exception),
                         "Size must be > 0.")

    """Perimeter tests."""

    def test_perimeter_zero(self):
        res_perimeter_zero = calculate.calc("triangle",
                                            "perimeter", [0, 0, 0])
        self.assertEqual(res_perimeter_zero, 0)

    def test_perimeter_positive(self):
        res_perimeter_1_pos = calculate.calc("triangle",
                                             "perimeter", [1, 1, 1])
        self.assertEqual(res_perimeter_1_pos, 3)

        res_perimeter_2_pos = calculate.calc("triangle",
                                             "perimeter", [6, 6, 6])
        self.assertEqual(res_perimeter_2_pos, 18)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "perimeter", [-1, -1, -1])
        self.assertEqual(str(context.exception),
                         "Size must be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "perimeter", [-6, -6, -6])
        self.assertEqual(str(context.exception),
                         "Size must be > 0.")


if __name__ == "__main__":
    unittest.main()
