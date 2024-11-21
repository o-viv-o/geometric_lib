"""Модуль с тестами для функций расчетов."""

from calculate import calc  

figs = ["circle", "square", "triangle"]
funcs = ["perimeter", "area"]

sizes = {
    "perimeter-circle": 1,
    "area-circle": 1,
    "perimeter-square": 1,
    "area-square": 1,
    "perimeter-triangle": 3,
    "area-triangle": 3,
}


def test_calc_circle_area():
    """Тест для вычисления площади круга."""
    assert calc("circle", "area", [1]) == 3.14 


def test_calc_circle_perimeter():
    """Тест для вычисления периметра круга."""
    assert calc("circle", "perimeter", [1]) == 6.28  


def test_calc_square_area():
    """Тест для вычисления площади квадрата."""
    assert calc("square", "area", [1]) == 1 


def test_calc_square_perimeter():
    """Тест для вычисления периметра квадрата."""
    assert calc("square", "perimeter", [1]) == 4  


def test_calc_triangle_area():
    """Тест для вычисления площади треугольника."""
    assert calc("triangle", "area", [3]) == 4.5  


def test_calc_triangle_perimeter():
    """Тест для вычисления периметра треугольника."""
    assert calc("triangle", "perimeter", [3]) == 9  


if __name__ == "__main__":
    import pytest
    pytest.main()
