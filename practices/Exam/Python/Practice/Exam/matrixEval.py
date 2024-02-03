def add_matrices(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def multiply_matrices_elementwise(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            result[i][j] = matrix1[i][j] * matrix2[i][j]
    return result

def multiply_matrices(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Input matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

# Perform addition
addition_result = add_matrices(matrix1, matrix2)
print("Addition Result:")
for row in addition_result:
    print(row)

# Perform element-wise multiplication
elementwise_multiplication_result = multiply_matrices_elementwise(matrix1, matrix2)
print("\nElement-wise Multiplication Result:")
for row in elementwise_multiplication_result:
    print(row)

# Perform matrix multiplication
matrix_multiplication_result = multiply_matrices(matrix1, matrix2)
print("\nMatrix Multiplication Result:")
for row in matrix_multiplication_result:
    print(row)
