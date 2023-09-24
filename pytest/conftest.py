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

@pytest.fixture(
    params=[TestCalc(), TestCalc(scientific=False)]
)
def basic_calc_fixture(request):
    return request.param

@pytest.fixture(scope="session", params=["basic", "scientific"])
def calc_mode(request):
    if request.param == "scientific":
        return TestCalc.with_mode("scientific")
    else:
        return TestCalc.with_mode("basic")