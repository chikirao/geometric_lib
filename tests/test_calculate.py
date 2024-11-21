import pytest
from calculate import calc


def test_calc_circle():
    assert calc("circle", "area", [1]) == pytest.approx(3.14159, 0.0001)
    assert calc("circle", "perimeter", [2]) == pytest.approx(12.56637, 0.0001)


def test_calc_square():
    assert calc("square", "area", [2]) == 4
    assert calc("square", "perimeter", [3]) == 12


def test_calc_invalid_figure():
    with pytest.raises(AssertionError):
        calc("triangle", "area", [1])


def test_calc_invalid_function():
    with pytest.raises(AssertionError):
        calc("circle", "volume", [1])
