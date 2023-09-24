import pytest


@pytest.mark.parametrize(
  argnames="a,b,expected",
  argvalues=[
      pytest.param(8, 3, pytest.approx(2.666666), marks=pytest.mark.smoke),
      pytest.param(-9, 0, 3, marks=[pytest.mark.xfail, pytest.mark.smoke]),
  ],
  ids=["general case", "zero division"]
)
def test_parametrized_with_marks(basic_calc, a, b, expected):
    assert basic_calc.divide(a, b) == expected