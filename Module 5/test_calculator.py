import unittest
import pytest

from calculator import add, subtract, multiply, divide

# UNITTEST: Two tests
class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_subtraction(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)


# PYTEST: Two tests
def test_pytest_multiplication():
    assert multiply(10, 5) == 50

def test_pytest_division():
    assert divide(10, 5) == 2

    with pytest.raises(ValueError):
        divide(10, 0)


if __name__ == "__main__":
    unittest.main()
