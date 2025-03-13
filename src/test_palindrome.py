# test_palindrome.py

import unittest
from palindrome_algorithms import is_palindrome_reversed, is_palindrome_recursive, is_palindrome_for_loop

class TestPalindromeAlgorithms(unittest.TestCase):
    def test_reversed(self):
        self.assertTrue(is_palindrome_reversed("racecar"))
        self.assertFalse(is_palindrome_reversed("hello"))
        self.assertTrue(is_palindrome_reversed("A man a plan a canal Panama"))

    def test_recursive(self):
        self.assertTrue(is_palindrome_recursive("racecar"))
        self.assertFalse(is_palindrome_recursive("hello"))
        self.assertTrue(is_palindrome_recursive("A man a plan a canal Panama"))

    def test_for_loop(self):
        self.assertTrue(is_palindrome_for_loop("racecar"))
        self.assertFalse(is_palindrome_for_loop("hello"))
        self.assertTrue(is_palindrome_for_loop("A man a plan a canal Panama"))

if __name__ == '__main__':
    unittest.main()