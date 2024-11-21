import pytest
from triangle import area, perimeter


def test_area():
    assert area(3, 4, 5) == 6
    assert area(6, 8, 10) == 12


def test_area_invalid():
    with pytest.raises(TypeError):
        area("not a number", 4, 5)
    with pytest.raises(TypeError):
        area(3, "not a number", 5)
    with pytest.raises(TypeError):
        area(3, 4, "not a number")


def test_perimeter():
    assert perimeter(3, 4, 5) == 12
    assert perimeter(6, 8, 10) == 24


def test_perimeter_invalid():
    with pytest.raises(TypeError):
        perimeter("not a number", 4, 5)
    with pytest.raises(TypeError):
        perimeter(3, "not a number", 5)
    with pytest.raises(TypeError):
        perimeter(3, 4, "not a number")
