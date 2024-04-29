# Reto-11
### Desarrolle la mayoría de ejercicios en clase, por cado punto resuelto en clase tendrá media décima en el examen 2 (créanme, las van a necesitar). Para cada punto cree un programa individual. Al finalizar suba todo a un repo y súbalo al canal reto_11 en slack.

#### 1. Desarrolle un programa que permita realizar la [suma/resta de matrices](https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
# Definición de la función para crear una matriz
def matrices(filas, columnas):
    matriz = []
    # Iteración para crear cada fila de la matriz
    for n in range(filas):
        fila = []
        # Iteración para ingresar los elementos de cada fila
        for num in range(columnas):
            total = int(input(f"Escribir el numero de la posicion ({n + 1}, {num + 1}): "))
            fila.append(total)
        matriz.append(fila)
    return matriz
# Definición de la función para sumar dos matrices
def suma_de_matriz(matriz1, matriz2):
    sumar = []
    # Iteración para recorrer las filas de las matrices
    for n in range(len(matriz1)):
        fila_sumar = []
        # Iteración para recorrer las columnas de las matrices
        for num in range(len(matriz1[0])):
            # Suma de los elementos correspondientes de ambas matrices
            sumar_valor = matriz1[n][num] + matriz2[n][num]
            fila_sumar.append(sumar_valor)
        sumar.append(fila_sumar)
    return sumar
# Definición de la función para restar dos matrices
def resta_de_matriz(matriz1, matriz2):
    restar = []
    # Iteración para recorrer las filas de las matrices
    for n in range(len(matriz1)):
        fila_restar = []
        # Iteración para recorrer las columnas de las matrices
        for num in range(len(matriz1[0])):
            # Resta de los elementos correspondientes de ambas matrices
            restar_valor = matriz1[n][num] - matriz2[n][num]
            fila_restar.append(restar_valor)
        restar.append(fila_restar)
    return restar
# Definición de la función para imprimir una matriz
def impr_matriz(matriz):
    for fila in matriz:
        print(fila)
if __name__ == "__main__":
    # Solicitar al usuario las dimensiones de las matrices
    filas1 = int(input("Escriba el numero de filas de la primera matriz"))
    columnas1 = int(input("Escriba el numero de columnas de la primera matriz"))
    filas2 = int(input("Escriba el numero de filas de la segunda matriz"))
    columnas2 = int(input("Escriba el numero de columnas de la segunda matriz"))
    # Crear las matrices
    print("\nEscriba la primera matriz")
    matriz1 = matrices(filas1, columnas1)
    print("\nEscriba la segunda matriz")
    matriz2 = matrices(filas2, columnas2)
    # Imprimir las matrices ingresadas
    print("\nLa primera matriz es:")
    impr_matriz(matriz1)
    print("\nLa segunda matriz es:")
    impr_matriz(matriz2)
    # Calcular y mostrar la suma de las matrices
    print("\nLa suma de las dos matrices es:")
    sumar = suma_de_matriz(matriz1, matriz2)
    impr_matriz(sumar)
    # Calcular y mostrar la resta de las matrices
    print("\nLa resta de las dos matrices es:")
    restar = resta_de_matriz(matriz1, matriz2)
    impr_matriz(restar)
```


#### 2. Desarrolle un programa que permita realizar el [producto de matrices](https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n_de_matrices). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
# Función para crear una matriz
def matrices(filas, columnas):
    matriz = []
    for n in range(filas):
        fila = []
        for num in range(columnas):
            total = int(input(f"Escribir el numero de la posicion ({n + 1}, {num + 1}): "))
            fila.append(total)
        matriz.append(fila)
    return matriz
# Función para realizar la multiplicación de matrices
def multiplicacion_de_matrices(matriz1, matriz2):
    # Verificar si las matrices son multiplicables
    if len(matriz1[0]) != len(matriz2):
        print("Operacion invalida. Las columnas de la matriz 1 deben ser iguales a las filas de la matriz 2")
        return
    # Inicializar matriz resultado
    resultado = []
    # Iterar sobre las filas de la primera matriz
    for n in range(len(matriz1)):
        fila_resultado = []
        # Iterar sobre las columnas de la segunda matriz
        for num in range(len(matriz2[0])):
            suma = 0
            # Iterar sobre los elementos de las matrices a multiplicar y sumar los productos
            for numero in range(len(matriz2)):
                suma += matriz1[n][numero] * matriz2[numero][num]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado
# Función para imprimir una matriz
def impr_matriz(matriz):
    for fila in matriz:
        print(fila)
if __name__ == "__main__":
    # Solicitar al usuario las dimensiones de las matrices
    filas1 = int(input("Escriba el numero de filas de la primera matriz"))
    columnas1 = int(input("Escriba el numero de columnas de la primera matriz"))
    filas2 = int(input("Escriba el numero de filas de la segunda matriz"))
    columnas2 = int(input("Escriba el numero de columnas de la segunda matriz"))
    # Crear las matrices
    print("\nEscribe la primera matriz")
    matriz1 = matrices(filas1, columnas1)
    print("\nEscribe la segunda matriz")
    matriz2 = matrices(filas2, columnas2)
    # Imprimir las matrices ingresadas
    print("\nLa primera matriz es:")
    impr_matriz(matriz1)
    print("\nLa segunda matriz es:")
    impr_matriz(matriz2)
    # Calcular y mostrar el producto de las matrices
    resultado = multiplicacion_de_matrices(matriz1, matriz2)
    if resultado:
        print("\nEl producto de las dos matrices es:")
        impr_matriz(resultado)
```


#### 3. Desarrolle un programa que permita obtener la  [matriz transpuesta](https://es.wikipedia.org/wiki/Matriz_transpuesta) de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
# Función para crear una matriz
def matrices(filas, columnas):
    matriz = []
    for n in range(filas):
        fila = []
        for num in range(columnas):
            total = int(input(f"Escribir el numero de la posicion ({n + 1}, {num + 1}): "))
            fila.append(total)
        matriz.append(fila)
    return matriz
# Función para obtener la matriz transpuesta
def obtener_matriz_transpuesta(matriz):
    # Obtener las dimensiones de la matriz original
    filas = len(matriz)
    columnas = len(matriz[0])
    # Inicializar la matriz transpuesta
    transpuesta = []
    # Iterar sobre las columnas de la matriz original
    for n in range(columnas):
        fila_adicional = []
        # Iterar sobre las filas de la matriz original
        for num in range(filas):
            # Agregar el elemento correspondiente a la nueva fila
            fila_adicional.append(matriz[num][n])
        # Agregar la nueva fila a la matriz transpuesta
        transpuesta.append(fila_adicional)
    return transpuesta
# Función para imprimir una matriz
def impr_matriz(matriz):
    for fila in matriz:
        print(fila)
if __name__ == "__main__":
    # Solicitar al usuario las dimensiones de la matriz
    filas = int(input("Escriba el numero de filas"))
    columnas = int(input("Escriba el numero de columnas"))
    print("\nEscribe la matriz")
    matriz = matrices(filas, columnas)
    # Imprimir la matriz original
    print("\nMatriz original:")
    impr_matriz(matriz)
    # Calcular y mostrar la matriz transpuesta
    print("\nMatriz transpuesta:")
    transpuesta = obtener_matriz_transpuesta(matriz)
    impr_matriz(transpuesta)
```


#### 4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
# Función para crear una matriz
def matrices(filas, columnas):
    matriz = []
    for n in range(filas):
        fila = []
        for num in range(columnas):
            total = int(input(f"Escribir el numero de la posicion ({n + 1}, {num + 1}): "))
            fila.append(total)
        matriz.append(fila)
    return matriz
# Función para sumar los elementos de una columna específica de la matriz
def sumar_columna(matriz, columna):
    suma = 0
    # Iterar sobre las filas de la matriz
    for fila in matriz:
        # Sumar el elemento de la columna especificada en cada fila
        suma += fila[columna]
    return suma
# Función para imprimir una matriz
def impr_matriz(matriz):
    for fila in matriz:
        print(fila)
if __name__ == "__main__":
    # Solicitar al usuario las dimensiones de la matriz
    filas = int(input("Escriba el numero de filas"))
    columnas = int(input("Escriba el numero de columnas"))
    print("\nEscribe la matriz")
    matriz = matrices(filas, columnas)
    # Imprimir la matriz ingresada
    print("\nMatriz:")
    impr_matriz(matriz)
    # Solicitar al usuario el número de la columna a sumar
    columna = int(input("Que numero de la columna desea sumar, comenzando desde 0"))
    # Calcular y mostrar la suma de los elementos de la columna especificada
    suma = sumar_columna(matriz, columna)
    print(f"\nLa suma de los elementos en la columna {columna} es: {suma}")
```


#### 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
# Función para crear una matriz
def matrices(filas, columnas):
    matriz = []
    # Iterar sobre las filas de la matriz
    for n in range(filas):
        fila = []
        # Iterar sobre las columnas de la matriz
        for num in range(columnas):
            # Solicitar al usuario el valor para cada posición de la matriz
            total = int(input(f"Escribir el numero de la posicion ({n + 1}, {num + 1}): "))
            fila.append(total)
        matriz.append(fila)
    return matriz
# Función para sumar los elementos de una fila específica de la matriz
def sumar_fila(matriz, fila):
    # Sumar los elementos de la fila utilizando la función sum de Python
    suma = sum(matriz[fila])
    return suma
# Función para imprimir una matriz
def impr_matriz(matriz):
    # Iterar sobre las filas de la matriz e imprimir cada fila
    for fila in matriz:
        print(fila)
if __name__ == "__main__":
    # Solicitar al usuario las dimensiones de la matriz
    filas = int(input("Escriba el numero de filas"))
    columnas = int(input("Escriba el numero de columnas"))
    print("\nEscribe la primera matriz")
    # Crear la matriz utilizando la función matrices
    matriz = matrices(filas, columnas)
    # Imprimir la matriz ingresada
    print("\nMatriz:")
    impr_matriz(matriz)
    # Solicitar al usuario el número de la fila a sumar
    fila = int(input("Que numero de la fila desea sumar, comenzando desde 0"))
    # Calcular y mostrar la suma de los elementos de la fila especificada
    suma = sumar_fila(matriz, fila)
    print(f"\nLa suma de los elementos en la fila {fila} es: {suma}")
```


**Nota:** Todos los puntos deben estar debidamente comentados y utilizar funciones para su desarrollo.
