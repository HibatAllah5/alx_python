#Function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    for i in matrix:
        print('\t'.join(map(str, i)))
