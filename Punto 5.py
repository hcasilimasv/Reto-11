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