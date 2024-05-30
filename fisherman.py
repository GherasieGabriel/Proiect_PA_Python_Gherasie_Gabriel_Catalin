import random
import time

class Lobster:
    def __init__(self, size=0, value=0):
        self.size = size
        self.value = value

class Matrix:
    def __init__(self, no_rows, no_cols):
        self.no_rows = no_rows
        self.no_cols = no_cols
        self.matrix = [0] * (no_rows * no_cols)

def scan_lobster(lobsters, no_lobster):
    for i in range(no_lobster):
        size = int(input(f"Introduceti dimensiunea homarului {i + 1}: "))
        if size <= 0:
            print("Dimensiunea introdusa nu este corecta. Va rog sa reintroduceti dimensiunea homarului.")
            i -= 1
            continue
        else:
            lobsters[i].size = size

            value = int(input(f"Introduceti valoarea homarului {i + 1}: "))
            if value <= 0:
                print("Valoarea introdusa nu este corecta. Va rog sa reintroduceti dimensiunea si valoarea homarului!")
                i -= 1
                continue
            else:
                lobsters[i].value = value

def generate_lobster(lobsters, no_lobster):
    dimension_limit = int(input("In ce interval de la 1 la n doriti sa se afle dimensiunea homariilor?")) - 1
    if dimension_limit <= 0:
        print("Dimensiune introdusa necorespunzatoare, se va actualiza automat la 20")
        dimension_limit = 20

    value_limit = int(input("In ce interval de la 1 la m doriti sa se afle valoarea homariilor?")) - 1
    if value_limit <= 0:
        print("Valoare introdusa necorespunzatoare, se va actualiza automat la 20")
        value_limit = 20

    random.seed(time.time())
    for i in range(no_lobster):
        lobsters[i].size = random.randint(1, dimension_limit)
        lobsters[i].value = random.randint(1, value_limit)

def print_lobster(lobsters, no_lobster):
    print("Homari:")
    for i in range(no_lobster):
        print(f"id: {i + 1} Dimensiune: {lobsters[i].size} Valoare: {lobsters[i].value} monede de aur")

def set_matrix_value(matrix, row_index, column_index, element_value):
    position = row_index * matrix.no_cols + column_index
    matrix.matrix[position] = element_value

def get_matrix_value(matrix, row_index, column_index):
    position = row_index * matrix.no_cols + column_index
    return matrix.matrix[position]

def print_matrix(matrix):
    print("=== Matrice ===")
    for i in range(matrix.no_rows):
        for j in range(matrix.no_cols):
            print(matrix.matrix[i * matrix.no_cols + j], end=" ")
        print()

def get_max(val1, val2):
    return max(val1, val2)

def lobster_descrete(lobsters, no_lobster, centimeters):
    matrix = Matrix(no_lobster + 1, centimeters + 1)

    for i in range(no_lobster + 1):
        for j in range(centimeters + 1):
            if i == 0 or j == 0:
                set_matrix_value(matrix, i, j, 0)
            elif lobsters[i - 1].size <= j:
                exclude_lobster = get_matrix_value(matrix, i - 1, j)
                include_lobster = lobsters[i - 1].value + get_matrix_value(matrix, i - 1, j - lobsters[i - 1].size)
                set_matrix_value(matrix, i, j, get_max(exclude_lobster, include_lobster))
            else:
                set_matrix_value(matrix, i, j, get_matrix_value(matrix, i - 1, j))

    lobster_value = get_matrix_value(matrix, matrix.no_rows - 1, matrix.no_cols - 1)
    print(f"Valoare maxima de monede de aur: {lobster_value}")