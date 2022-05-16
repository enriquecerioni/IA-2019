import numpy as np


def print_matrix(matrix):
    print("----------------------------")
    for i in range(8):
        for j in range(8):
            print(matrix[i][j], end=" ")
        print()
    print("----------------------------")


def validate(matrix, row, col):

    # Valido si es posible colocar una reina en el lugar, en caso negativo devuelvo un false

    for i in range(8):
        if matrix[row][i] == 1:
            return False

    for j in range(8):
        if matrix[j][col] == 1:
            return False

    # Verifico las diagonales comparando las reinas y sus valores absolutos

    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                delta_x = abs(row - i)
                delta_y = abs(col - j)
                if delta_x == delta_y:
                    return False

    return True


def solver(table, row):
    # Cuento reinas
    if row >= 8:
        return True

    for j in range(8):
        if validate(table, row, j):
            table[row][j] = 1
            print_matrix(A)
            # Coloco demas reinas
            if solver(table, row + 1):
                return True
            table[row][j] = 0

    return False


A = np.zeros((8, 8), dtype=int)

# Paso tablero de ajedrez y la fila en 0

if not solver(A, 0):
    print("No existe solucion")

else:
    print_matrix(A)
