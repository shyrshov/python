import pytest

def test_add_positive_numbers(basic_calc):
  assert basic_calc.add(30, 3) == 33


def test_add_negative_numbers(basic_calc):
  assert basic_calc.add(-12, -2) == -14


def test_substract_positive_numbers(basic_calc):
  assert basic_calc.subtract(30, 3) == 27


def test_subtract_negative_numbers(basic_calc):
  assert basic_calc.subtract(-30, -3) == -27


def test_multiply_positive_numbers(basic_calc):
  assert basic_calc.multiply(5, 4) == 20


def test_multiply_negative_numbers(basic_calc):
  assert basic_calc.multiply(-3, -5) == 15


def test_divide_positive_numbers(basic_calc):
  assert basic_calc.divide(8, 3) == 2.6666666666666665


def test_divide_negative_numbers(basic_calc):
  assert basic_calc.divide(-9, -3) == 3


def test_power_positive_numbers(scientific_calc):
  assert scientific_calc.power(4, 3) == 64


def test_power_negative_numbers(scientific_calc):
  assert scientific_calc.power(-3, -2) == 0.1111111111111111


def test_factorial_positive_numbers(scientific_calc):
  assert scientific_calc.factorial(5) == 120


def test_factorial_negative_numbers(scientific_calc):
  with pytest.raises(ValueError):
        scientific_calc.factorial(-5)
