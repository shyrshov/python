import pytest

pytestmark = pytest.mark.skip("Low priority functionality")

def test_memory_without_operation(basic_calc):
    basic_calc.save_to_memory(3)
    assert basic_calc.recall_memory() == 3
 
def test_memory_with_operation(basic_calc):
    basic_calc.save_to_memory(3)
    basic_calc.add(3, 33)
    assert basic_calc.recall_memory() == 3