# palindrome_algorithms.py
def clean_string(s):
    """Limpia la cadena: elimina espacios y convierte a minúsculas."""
    return ''.join(char.lower() for char in s if char.isalnum())

def is_palindrome_reversed(s):
    """
    Solution 1: Comparing a String With Its Reversed Version.
    """
    cleaned_s = clean_string(s)
    return cleaned_s == cleaned_s[::-1]

def is_palindrome_recursive(s):
    """
    Solution 2: Recursion (con límite de tamaño).
    """
    cleaned_s = clean_string(s)
    if len(cleaned_s) > 750:  # Limitar el tamaño de la cadena
        raise ValueError("El algoritmo recursivo no admite cadenas de más de 750 caracteres.")
    cleaned_s = cleaned_s.lower()
    if len(cleaned_s) <= 1:
        return True
    if cleaned_s[0] != cleaned_s[-1]:
        return False
    return is_palindrome_recursive(cleaned_s[1:-1])

def is_palindrome_for_loop(s):
    """
    Solution 3: for Loop.
    """
    cleaned_s = clean_string(s)
    length = len(cleaned_s)
    for i in range(length // 2):
        if cleaned_s[i] != cleaned_s[length - i - 1]:
            return False
    return True