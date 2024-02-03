import numpy as np


def sort_matrix_by_second_row(matrix):
    # Get the indices that would sort the second row
    sorted_indices = np.argsort(matrix[1])

    # Sort the matrix based on the sorted indices
    sorted_matrix = matrix[:, sorted_indices]

    return sorted_matrix


# Generate a random matrix
rows = 3
cols = 5
random_matrix = np.random.randint(0, 100, size=(rows, cols))

print("Random Matrix:")
print(random_matrix)

# Sort the matrix with respect to the second row
sorted_matrix = sort_matrix_by_second_row(random_matrix)

print("\nSorted Matrix with respect to the second row:")
print(sorted_matrix)
