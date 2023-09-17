import pytest

def verify_last_results(basic_calc):
  basic_calc.add(99, 1)
  basic_calc.subtract(55, 5)
  assert basic_calc.get_last_results() == [100, 50]