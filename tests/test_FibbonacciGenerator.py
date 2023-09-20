import unittest

from src.FibbonacciGenerator import generate_fibonacci_sequence


class TestGenerateFibonacciSequenceRecursive(unittest.TestCase):
    def test_generate_fibonacci_sequence_with_0_elements(self):
        result = generate_fibonacci_sequence(0)
        self.assertEqual(result, [])

    def test_generate_fibonacci_sequence_with_1_element(self):
        result = generate_fibonacci_sequence(1)
        self.assertEqual(result, [0])

    def test_generate_fibonacci_sequence_with_2_elements(self):
        result = generate_fibonacci_sequence(2)
        self.assertEqual(result, [0, 1])

    def test_generate_fibonacci_sequence_with_5_elements(self):
        result = generate_fibonacci_sequence(5)
        self.assertEqual(result, [0, 1, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
