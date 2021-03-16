import pytest


from geo_figure import Circle


class CircleTest:


  def test_circle_initialization(self, my_circle):
    assert my_circle

  @pytest.mark.parametrize("new_circle", [Circle, 3])
  def test_rgc(self, new_circle):
     assert new_circle.this_geo() == Circle

  def test_c_area_n_to_p(self, my_circle):
    with pytest.raises(ValueError):
     my_circle.p_area = 'a'

  @pytest.mark.parametrize("buggy", [0, 3, "q"])
  def test_circle_true(self, my_circle, buggy):
         my_circle.circle_true = buggy

  @pytest.mark.parametrize("alt_area", [4, "o"])
  def test_add_area(self, my_circle, alt_area):
      my_circle.add_area(alt_area)