def is_palindrome(number: int) -> bool:
    """
    Check if a number is a palindrome.

    Args:
        number: The number to check.

    Returns:
        True if the number is a palindrome, False otherwise.

    Raises:
        ValueError: If the input is not a non-negative integer.
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")

    str_num = str(number)
    return str_num == str_num[::-1]

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(12321))
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(123456))
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            is_palindrome(-121)
        with self.assertRaises(ValueError):
            is_palindrome(3.14)
        with self.assertRaises(ValueError):
            is_palindrome("121")
