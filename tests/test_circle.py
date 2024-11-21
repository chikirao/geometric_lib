import pytest
from circle import area, perimeter


def test_area():
    assert area(1) == pytest.approx(3.14159, 0.0001)
    assert area(2) == pytest.approx(12.56637, 0.0001)


def test_area_invalid():
    with pytest.raises(TypeError):
        area("not a number")


def test_perimeter():
    assert perimeter(1) == pytest.approx(6.28318, 0.0001)
    assert perimeter(2) == pytest.approx(12.56637, 0.0001)


def test_perimeter_invalid():
    with pytest.raises(TypeError):
        perimeter("not a number")
