import pytest


def test_multiply_positive_with_reset(basic_calc_reset, basic_calc):
    assert len(basic_calc.get_last_results()) == 0
    assert basic_calc.multiply(1, 3) == 3

def test_subtract_negative_with_reset(basic_calc_reset, basic_calc):
    assert len(basic_calc.get_last_results()) == 0
    assert basic_calc.subtract(-30, -3) == -27