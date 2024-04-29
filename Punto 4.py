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