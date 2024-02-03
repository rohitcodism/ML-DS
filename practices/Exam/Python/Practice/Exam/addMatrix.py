import numpy as np

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    return np.array(matrix)

def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def add_matrices(matrix1, matrix2):
    return matrix1 + matrix2

# Read matrices from files
matrix1 = read_matrix_from_file('matrix1.txt')
matrix2 = read_matrix_from_file('matrix2.txt')

# Add matrices
result_matrix = add_matrices(matrix1, matrix2)

# Write matrices and result to file
write_matrix_to_file(matrix1, 'matrix1_result.txt')
write_matrix_to_file(matrix2, 'matrix2_result.txt')
write_matrix_to_file(result_matrix, 'result_matrix.txt')

print("Matrices and result have been stored in files.")
