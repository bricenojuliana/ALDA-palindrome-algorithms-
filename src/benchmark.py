# benchmark.py

import time
import csv
import matplotlib.pyplot as plt
import numpy as np
from palindrome_generator import generate_palindrome
from executor import run_algorithms

def run_benchmark(lengths, repetitions=11):
    """Ejecuta el benchmark para los algoritmos."""
    results = []
    for length in lengths:
        s = generate_palindrome(length)
        try:
            reversed_time, recursive_time, for_loop_time = run_algorithms(s, repetitions)
            results.append((length, reversed_time, recursive_time, for_loop_time))
            # Manejar el caso en que recursive_time sea None
            recursive_time_str = f"{recursive_time:.6f}s" if recursive_time is not None else "N/A"
            print(f"Longitud: {length}, Reversed: {reversed_time:.6f}s, Recursivo: {recursive_time_str}, For Loop: {for_loop_time:.6f}s")
        except ValueError as e:
            print(f"Longitud: {length}, Error: {e}")
            results.append((length, None, None, None))  # Registrar un error para esta longitud
    return results

def save_results_to_csv(results, filename="benchmark_results.csv"):
    """Guarda los resultados en un archivo CSV."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Longitud", "Reversed", "Recursivo", "For Loop"])
        for result in results:
            writer.writerow(result)

def plot_results(results):
    """Genera gráficas a partir de los resultados."""
    lengths = [result[0] for result in results]
    reversed_times = [result[1] for result in results]
    recursive_times = [result[2] for result in results]
    for_loop_times = [result[3] for result in results]

    # Filtrar longitudes hasta 750 para el algoritmo recursivo
    max_length_for_recursive = 750
    filtered_lengths = [length for length in lengths if length <= max_length_for_recursive]
    filtered_reversed_times = [time for length, time in zip(lengths, reversed_times) if length <= max_length_for_recursive]
    filtered_recursive_times = [time for length, time in zip(lengths, recursive_times) if length <= max_length_for_recursive]
    filtered_for_loop_times = [time for length, time in zip(lengths, for_loop_times) if length <= max_length_for_recursive]

    # Gráfica 1: Comparación de los tres algoritmos (hasta 750 caracteres)
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_lengths, filtered_reversed_times, label="Reversed", marker="o", linestyle="-", color="blue")
    plt.plot(filtered_lengths, filtered_recursive_times, label="Recursivo", marker="s", linestyle="-", color="green")
    plt.plot(filtered_lengths, filtered_for_loop_times, label="For Loop", marker="^", linestyle="-", color="red")
    plt.xlabel("Longitud de la cadena")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de Algoritmos de Palíndromos (Hasta 750 caracteres)")
    plt.legend()
    plt.grid(True)
    plt.savefig("tiempo_vs_longitud_hasta_750.png")  # Guardar la gráfica
    plt.show()

    # Gráfica 2: Comparación de Reversed y For Loop (todas las longitudes)
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, reversed_times, label="Reversed", marker="o", linestyle="-", color="blue")
    plt.plot(lengths, for_loop_times, label="For Loop", marker="^", linestyle="-", color="red")
    plt.xlabel("Longitud de la cadena")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de Algoritmos de Palíndromos (Reversed y For Loop)")
    plt.legend()
    plt.grid(True)
    plt.savefig("tiempo_vs_longitud_reversed_for_loop.png")  # Guardar la gráfica
    plt.show()

    # Gráfica 3: Tiempo de ejecución normalizado (hasta 750 caracteres)
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_lengths, np.array(filtered_reversed_times) / np.array(filtered_lengths), label="Reversed", marker="o", linestyle="-", color="blue")
    plt.plot(filtered_lengths, np.array(filtered_recursive_times) / np.array(filtered_lengths), label="Recursivo", marker="s", linestyle="-", color="green")
    plt.plot(filtered_lengths, np.array(filtered_for_loop_times) / np.array(filtered_lengths), label="For Loop", marker="^", linestyle="-", color="red")
    plt.xlabel("Longitud de la cadena")
    plt.ylabel("Tiempo de ejecución normalizado (segundos/n)")
    plt.title("Tiempo de Ejecución Normalizado (Hasta 750 caracteres)")
    plt.legend()
    plt.grid(True)
    plt.savefig("tiempo_normalizado_hasta_750.png")  # Guardar la gráfica
    plt.show()

    # Gráfica 4: Tiempo de ejecución normalizado (Reversed y For Loop, todas las longitudes)
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, np.array(reversed_times) / np.array(lengths), label="Reversed", marker="o", linestyle="-", color="blue")
    plt.plot(lengths, np.array(for_loop_times) / np.array(lengths), label="For Loop", marker="^", linestyle="-", color="red")
    plt.xlabel("Longitud de la cadena")
    plt.ylabel("Tiempo de ejecución normalizado (segundos/n)")
    plt.title("Tiempo de Ejecución Normalizado (Reversed y For Loop)")
    plt.legend()
    plt.grid(True)
    plt.savefig("tiempo_normalizado_reversed_for_loop.png")  # Guardar la gráfica
    plt.show()

    # Gráfica 5: Tiempo de ejecución en escala logarítmica (Reversed y For Loop)
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, reversed_times, label="Reversed", marker="o", linestyle="-", color="blue")
    plt.plot(lengths, for_loop_times, label="For Loop", marker="^", linestyle="-", color="red")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Longitud de la cadena (log)")
    plt.ylabel("Tiempo de ejecución (log)")
    plt.title("Tiempo de Ejecución en Escala Logarítmica (Reversed y For Loop)")
    plt.legend()
    plt.grid(True)
    plt.savefig("tiempo_logaritmico_reversed_for_loop.png")  # Guardar la gráfica
    plt.show()

    # Gráfica 6: Tiempo de ejecución acumulado (Reversed y For Loop)
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, np.cumsum(reversed_times), label="Reversed", marker="o", linestyle="-", color="blue")
    plt.plot(lengths, np.cumsum(for_loop_times), label="For Loop", marker="^", linestyle="-", color="red")
    plt.xlabel("Longitud de la cadena")
    plt.ylabel("Tiempo de ejecución acumulado (segundos)")
    plt.title("Tiempo de Ejecución Acumulado (Reversed y For Loop)")
    plt.legend()
    plt.grid(True)
    plt.savefig("tiempo_acumulado_reversed_for_loop.png")  # Guardar la gráfica
    plt.show()

def main():
    lengths = [10, 100, 250, 500, 750, 1000, 10000, 100000]  # Tamaños de entrada
    repetitions = 11  # Número de repeticiones para calcular la mediana

    # Ejecutar el benchmark
    results = run_benchmark(lengths, repetitions)

    # Guardar los resultados en un archivo CSV
    save_results_to_csv(results)

    # Generar gráficas
    plot_results(results)

if __name__ == '__main__':
    main()