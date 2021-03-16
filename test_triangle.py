import pytest


from geo_figure import Triangle

class TriangleTest:

    def test_triangle_initialization(self, my_triangle):
          assert my_triangle

    @pytest.mark.parametrize("new_triangle", [Triangle, 3])
    def test_tgc(self, new_triangle):
        assert new_triangle.this_geo() == Triangle


    def test_tp_area_n_to_p(self, my_triangle):
            with pytest.raises(ValueError):
             my_triangle.p_area = 'a'

    @pytest.mark.parametrize("angles_num", [3, 2, "b"])
    def test_p_triangles(self, my_triangle, angles_num):
            my_triangle.p_triangles = angles_num

    @pytest.mark.parametrize("alt_area", [4, "c"])
    def test_add_area(self, my_triangle, alt_area):
        my_triangle.add_area(alt_area)




