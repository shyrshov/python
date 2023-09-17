import pytest
from app.test_calc import TestCalc


@pytest.fixture(scope="session")
def basic_calc():
    return TestCalc.basic_calc()


@pytest.fixture(scope="session")
def scientific_calc():
    return TestCalc.scientific_calc()


@pytest.fixture(scope="function")
def basic_calc_reset(basic_calc):
    basic_calc.reset()
    yield


