#Function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    response = []
    for row in matrix:
        sub_matrix = map(lambda num: num**2, row)
        response.append(list(sub_matrix))
    return response
