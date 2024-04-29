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