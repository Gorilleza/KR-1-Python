from typing import List
import unittest

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate the first n Fibonacci numbers.

    Args:
        n: The number of Fibonacci numbers to generate.

    Returns:
        A list containing the first n Fibonacci numbers.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence[:n]

class TestFibonacci(unittest.TestCase):
    def test_generate_fibonacci(self):
        self.assertEqual(generate_fibonacci(1), [0])
        self.assertEqual(generate_fibonacci(2), [0, 1])
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(generate_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            generate_fibonacci(0)
        with self.assertRaises(ValueError):
            generate_fibonacci(-5)
        with self.assertRaises(ValueError):
            generate_fibonacci(3.14)
        with self.assertRaises(ValueError):
            generate_fibonacci("5")
