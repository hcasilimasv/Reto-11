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