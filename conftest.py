import pytest

from geo_figure import Triangle
from geo_figure import Rectangle
from geo_figure import Quadrate
from geo_figure import Circle

@pytest.fixture(scope="function")
def my_triangle():
    return Triangle(name="Треугольник", area=10, angles=3, perimeter=24)

@pytest.fixture(scope="function")
def my_rectangle():
    return Rectangle(name="Прямоугольник", area=15, angles=4, perimeter=30)

@pytest.fixture(scope="function")
def my_quadrate():
    return Quadrate(name="Квадрат", area=16, angles=4, perimeter=16)

@pytest.fixture(scope="function")
def my_circle():
    return Circle(name="Круг", area=4, angles=0, perimeter=26)