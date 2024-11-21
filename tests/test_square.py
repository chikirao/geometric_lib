import pytest
from square import area, perimeter


def test_area():
    assert area(2) == 4
    assert area(3) == 9


def test_area_invalid():
    with pytest.raises(TypeError):
        area("not a number")


def test_perimeter():
    assert perimeter(2) == 8
    assert perimeter(3) == 12


def test_perimeter_invalid():
    with pytest.raises(TypeError):
        perimeter("not a number")
