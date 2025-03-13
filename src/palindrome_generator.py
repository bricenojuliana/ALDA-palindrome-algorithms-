# palindrome_generator.py

import random
import string

def generate_palindrome(length):
    half = ''.join(random.choice(string.ascii_lowercase) for _ in range(length // 2))
    return half + half[::-1] if length % 2 == 0 else half + random.choice(string.ascii_lowercase) + half[::-1]