import pytest

from geo_figure import Quadrate

class QuadrateTest:

    def test_quadrate_initialization(self, my_quadrate):
        assert my_quadrate

    @pytest.mark.parametrize("new_quadrate", [Quadrate, 3])
    def test_rgc(self, new_quadrate):
        assert new_quadrate.this_geo() == Quadrate

    @pytest.mark.parametrize("angles_num", [3, 0, "l"])
    def test_r_angles(self, my_quadrate, angles_num):
        my_quadrate.r_q_angles = angles_num

    def test_q_sides(self, my_quadrate):
        assert my_quadrate.q_sides()

    @pytest.mark.parametrize("alt_area", [4, "h"])
    def test_qadd_area(self, my_quadrate, alt_area):
        my_quadrate.add_area(alt_area)