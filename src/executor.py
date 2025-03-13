# executor.py

import time
import numpy as np
from palindrome_algorithms import is_palindrome_reversed, is_palindrome_recursive, is_palindrome_for_loop

def measure_time(algorithm, s):
    """Mide el tiempo de ejecución de un algoritmo."""
    start_time = time.time()
    algorithm(s)
    end_time = time.time()
    return end_time - start_time

def calculate_median_time(algorithm, s, repetitions=11):
    """Calcula la mediana del tiempo de ejecución de un algoritmo."""
    times = []
    for _ in range(repetitions):
        try:
            elapsed_time = measure_time(algorithm, s)
            times.append(elapsed_time)
        except ValueError as e:
            print(f"Error: {e}")
            return None  # Si hay un error, devolver None
    return np.median(times)

def run_algorithms(s, repetitions=11):
    """Ejecuta los algoritmos y devuelve la mediana del tiempo de ejecución."""
    reversed_time = calculate_median_time(is_palindrome_reversed, s, repetitions)
    recursive_time = calculate_median_time(is_palindrome_recursive, s, repetitions)
    for_loop_time = calculate_median_time(is_palindrome_for_loop, s, repetitions)
    return reversed_time, recursive_time, for_loop_time