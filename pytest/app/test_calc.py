import time


def require_scientific_mode(func):
    def wrapper(self, *args, **kwargs):
        if not self.scientific:
            raise ValueError("Method can only be called when scientific=True")
        return func(self, *args, **kwargs)

    return wrapper


class TestCalc:
    """
    Creates two different types of TestCalc():

    1. basic_calc = TestCalc.basic_calc()
        includes all methods except power() and factorial()

    2. scientific_calc = TestCalc.scientific_calc()
        includes all methods
    """
    __test__ = False

    def __init__(self, scientific=False, last_results_count=3):
        self.memory = 0
        self.last_results = []
        self.scientific = scientific
        self.last_results_count = last_results_count

    @classmethod
    def basic_calc(cls):
        return cls()

    @classmethod
    def scientific_calc(cls):
        return cls(scientific=True)

    @classmethod
    def with_mode(cls, mode):
        if mode not in ("basic", "scientific"):
            raise Exception(f"Not supported mode '{mode}'")
        return cls(scientific=mode == "scientific")

    def add(self, a, b):
        result = a + b
        self._update_last_results(result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._update_last_results(result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._update_last_results(result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._update_last_results(result)
        return result

    @require_scientific_mode
    def power(self, base, exponent):
        time.sleep(0.2)
        result = base ** exponent
        self._update_last_results(result)
        return result

    @require_scientific_mode
    def factorial(self, n):
        time.sleep(0.1)

        def perform(i):
            if i < 0:
                raise ValueError("Factorial is not defined for negative numbers")
            if i == 0 or i == 1:
                return 1
            return i * perform(i - 1)

        result = perform(n)
        self._update_last_results(result)
        return result

    def save_to_memory(self, value):
        self.memory = value

    def recall_memory(self):
        return self.memory

    def reset(self):
        self.memory = 0
        self.last_results = []

    def get_last_results(self):
        return self.last_results

    def _update_last_results(self, result):
        if len(self.last_results) >= self.last_results_count:
            self.last_results.pop(0)
        self.last_results.append(result)

    def scientific(self, func):
        if not self.scientific:
            raise Exception("Method available in scientific mode")
        func(self)
