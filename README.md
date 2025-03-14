# Análisis de Algoritmos de Palíndromos

Este repositorio contiene un análisis comparativo de tres algoritmos para verificar si una cadena es un palíndromo. Los algoritmos implementados son:
1. **Reversed**: Compara la cadena con su versión invertida.
2. **Recursivo**: Verifica recursivamente si la cadena es un palíndromo.
3. **For Loop**: Usa un bucle para comparar los caracteres desde los extremos hacia el centro.

El proyecto incluye:
- Implementación de los algoritmos en Python.
- Pruebas unitarias para verificar su correcto funcionamiento.
- Un benchmark para medir el tiempo de ejecución de cada algoritmo.
- Gráficas comparativas del rendimiento de los algoritmos.
- Un Jupyter Notebook con el análisis detallado y las conclusiones.


## Estructura del Repositorio

```
palindrome-project/
├── src/
│   ├── palindrome_algorithms.py   # Implementación de los algoritmos.
│   ├── palindrome_generator.py    # Generador de cadenas palindrómicas.
│   ├── executor.py                # Medición del tiempo de ejecución.
│   ├── benchmark.py               # Ejecución del benchmark.
│   ├── test_palindrome.py         # Pruebas unitarias.
├── analysis.ipynb                 # Notebook con el análisis y gráficas.
├── graficas/                      # Gráficas generadas.
│   ├── tiempo_vs_longitud_hasta_750.png
│   ├── tiempo_vs_longitud_reversed_for_loop.png
│   ├── tiempo_normalizado_hasta_750.png
│   ├── tiempo_normalizado_reversed_for_loop.png
│   ├── tiempo_logaritmico_reversed_for_loop.png
│   ├── tiempo_acumulado_reversed_for_loop.png
├── README.md                      # Este archivo.
├── requirements.txt               # Dependencias del proyecto.
```


## Requisitos

Para ejecutar este proyecto, necesitas:

- Python 3.8 o superior.
- Bibliotecas de Python: `matplotlib`, `numpy`, `coverage`.

Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```


## Cómo Usar

### Ejecutar el Benchmark

Para ejecutar el benchmark y generar las gráficas, ejecuta el siguiente comando:

```bash
python src/benchmark.py
```

Esto generará las gráficas en la carpeta `graficas/` y guardará los resultados en un archivo CSV (`benchmark_results.csv`).

### Ejecutar las Pruebas Unitarias

Para ejecutar las pruebas unitarias y verificar que los algoritmos funcionan correctamente, usa:

```bash
python -m unittest src/test_palindrome.py
```

### Medir la Cobertura del Código

Para medir la cobertura del código, ejecuta:

```bash
coverage run -m unittest src/test_palindrome.py
coverage report -m
```

### Abrir el Notebook de Análisis

Para ver el análisis detallado y las gráficas, abre el Jupyter Notebook `analysis.ipynb`:

```bash
jupyter notebook analysis.ipynb
```


## Resultados y Conclusiones

### Gráficas Generadas

1. **Comparación de los tres algoritmos (hasta 750 caracteres)**:
   - Muestra el tiempo de ejecución de los algoritmos **Reversed**, **Recursivo** y **For Loop** para cadenas de hasta 750 caracteres.
   - El algoritmo **Recursivo** es mucho más lento que los otros dos.

2. **Comparación de Reversed y For Loop (todas las longitudes)**:
   - Compara los algoritmos **Reversed** y **For Loop** para cadenas de hasta 100,000 caracteres.
   - El algoritmo **Reversed** es el más eficiente en todos los casos.

3. **Tiempo de ejecución normalizado (hasta 750 caracteres)**:
   - Muestra el tiempo de ejecución dividido por la longitud de la cadena.
   - El algoritmo **Recursivo** tiene el mayor tiempo normalizado.

4. **Tiempo de ejecución normalizado (Reversed y For Loop, todas las longitudes)**:
   - Compara la eficiencia relativa de los algoritmos **Reversed** y **For Loop**.
   - El algoritmo **Reversed** mantiene su ventaja en eficiencia.

5. **Tiempo de ejecución en escala logarítmica (Reversed y For Loop)**:
   - Visualiza las diferencias en órdenes de magnitud.
   - El algoritmo **Reversed** es claramente el más eficiente.

6. **Tiempo de ejecución acumulado (Reversed y For Loop)**:
   - Muestra el impacto total del rendimiento de los algoritmos.
   - El algoritmo **Reversed** tiene el menor tiempo acumulado.

### Conclusiones

- **Reversed**: Es el más eficiente en tiempo de ejecución, ideal para la mayoría de los casos prácticos.
- **For Loop**: Es una buena alternativa cuando la memoria es un factor crítico, aunque su rendimiento es ligeramente inferior.
- **Recursivo**: Es mucho más lento y tiene limitaciones importantes debido al límite de recursión en Python. Solo es viable para cadenas pequeñas o fines educativos.


## Licencia

Este proyecto está bajo la licencia **MIT**. Para más detalles, consulta el archivo [LICENSE](LICENSE).
