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