import pytest

from geo_figure import Rectangle

class RectangleTest:

    def test_rectangle_initialization(self, my_rectangle):
        assert my_rectangle

    @pytest.mark.parametrize("new_rectangle", [Rectangle, 3])
    def test_rgc(self, new_rectangle):
        assert new_rectangle.this_geo() == Rectangle

    def test_rp_area_n_to_p(self, my_rectangle):
            with pytest.raises(ValueError):
              my_rectangle.p_area = 'g'

    @pytest.mark.parametrize("angles_num", [3, 0, "k"])
    def test_r_angles(self, my_rectangle, angles_num):
        my_rectangle.r_q_angles = angles_num

    @pytest.mark.parametrize("alt_area", [4, "c"])
    def test_radd_area(self, my_rectangle, alt_area):
        my_rectangle.add_area(alt_area)