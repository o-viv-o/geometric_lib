import unittest
from math import pi
from calculate import calc


class TestCalcPerimeter(unittest.TestCase):
    def test_calc_circle_perimeter(self):
        # Arrange
        fig = "circle"
        func = "perimeter"
        size = [3]
        expected_result = 2 * pi * 3

        # Ac
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_square_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [3]
        expected_result = 12

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_triangle_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [10, 12, 15]
        expected_result = 37

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)


class TestCalcArea(unittest.TestCase):
    def test_calc_circle_area(self):
        fig = "circle"
        func = "area"
        size = [5]
        expected_result = 5 * 5 * pi

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_square_area(self):
        fig = "square"
        func = "area"
        size = [10]
        expected_result = 100

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_triangle_area(self):
        fig = "triangle"
        func = "area"
        size = [9, 12, 15]
        expected_result = 18

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)


class TestCalcIntegerNegative(unittest.TestCase):
    def test_calc_values_triangle(self):
        fig = "triangle"
        func = "area"
        size = [-3, 4, 5]
        expected_result = "Size must be > 0."

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_values_circle(self):
        fig = "circle"
        func = "area"
        size = [-1]
        expected_result = "Radius must be > 0."

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_values_square(self):
        fig = "square"
        func = "area"
        size = [-6]
        expected_result = "Size must be > 0."

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)
