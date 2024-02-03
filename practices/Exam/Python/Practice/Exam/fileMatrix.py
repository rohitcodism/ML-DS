def read_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the elements row-wise:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Error: Number of elements in the row does not match the number of columns.")
            return None
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Matrices must have the same dimensions for addition.")
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

# Read matrices from the user
print("Enter the first matrix:")
matrix1 = read_matrix()
print("Enter the second matrix:")
matrix2 = read_matrix()

# Add matrices
if matrix1 and matrix2:
    result_matrix = add_matrices(matrix1, matrix2)
    if result_matrix:
        print("Resultant Matrix after Addition:")
        for row in result_matrix:
            print(row)

        # Write matrices and result to a file
        write_matrix_to_file(matrix1, 'matrix1.txt')
        write_matrix_to_file(matrix2, 'matrix2.txt')
        write_matrix_to_file(result_matrix, 'result_matrix.txt')
        print("Matrices and result have been stored in files: matrix1.txt, matrix2.txt, result_matrix.txt")
