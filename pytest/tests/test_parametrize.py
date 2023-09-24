import pytest

@pytest.mark.parametrize(
    argnames="operation,number_one,number_two,expected",
    argvalues=[
        ("add", 30, 3, 33),
        ("add", -12, -2, -14),
        ("subtract", 30, 3, 27),
        ("subtract", -30, -3, -27),
        ("multiply", 5, 4, 20),
        ("multiply", -3, -5, 15),
        ("divide", 8, 3, 2.6666666666666665),
        ("divide", -9, -3, 3),
        ("power", 4, 3, 64),
        ("power", -3, -2, 0.1111111111111111)
    ],
    ids=[
        "Add positive check: 30 + 3 == 33",
        "Add negative check: -12 + (-2) = -14",
        "Subsract positive check: 30 - 3 = 27",
        "Subsract negative check: -30 -(-3) = 27",
        "Multiply positive check: 5 * 4 = 20",
        "Multiply negative check: -3 * (-5) = 15",
        "Divide positive check: 8 / 3 = 2.666666",
        "Divide negative check: -9 / (-3) = 3",
        "Power positive check: 4 ^ 3 = 64",
        "Power negative check: -3 ^ (-2) = 0.1111111111111111"
    ]
)
def test_operations(scientific_calc, operation, number_one, number_two, expected):
    if operation.startswith("add"):
        result = scientific_calc.add(number_one, number_two)
    elif operation.startswith("subtract"):
        result = scientific_calc.subtract(number_one, number_two)
    elif operation.startswith("multiply"):
        result = scientific_calc.multiply(number_one, number_two)
    elif operation.startswith("divide"):
        result = scientific_calc.divide(number_one, number_two)
    elif operation.startswith("power"):
        result = scientific_calc.power(number_one, number_two)
    assert result == expected

@pytest.mark.parametrize(
    argnames="operation,number_one,number_two,expected",
    argvalues=[
        ("add", 30, 3, 33),
        ("add", -12, -2, -14),
        ("subtract", 30, 3, 27),
        ("subtract", -30, -3, -27),
        ("multiply", 5, 4, 20),
        ("multiply", -3, -5, 15),
        ("divide", 8, 3, 2.6666666666666665),
        ("divide", -9, -3, 3)
    ],
    ids=[
        "Add positive check: 30 + 3 == 33",
        "Add negative check: -12 + (-2) = -14",
        "Subsract positive check: 30 - 3 = 27",
        "Subsract negative check: -30 -(-3) = 27",
        "Multiply positive check: 5 * 4 = 20",
        "Multiply negative check: -3 * (-5) = 15",
        "Divide positive check: 8 / 3 = 2.666666",
        "Divide negative check: -9 / (-3) = 3"
    ]
)
def test_operations_fixture(basic_calc_fixture, operation, number_one, number_two, expected):
    if operation.startswith("add"):
        result = basic_calc_fixture.add(number_one, number_two)
    elif operation.startswith("subtract"):
        result = basic_calc_fixture.subtract(number_one, number_two)
    elif operation.startswith("multiply"):
        result = basic_calc_fixture.multiply(number_one, number_two)
    elif operation.startswith("divide"):
        result = basic_calc_fixture.divide(number_one, number_two)
    assert result == expected


def test_operations_hook(calc_mode):
    assert calc_mode.add(7, 3) == 10