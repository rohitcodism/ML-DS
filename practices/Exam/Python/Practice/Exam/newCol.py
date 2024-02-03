import numpy as np


def delete_and_insert_column(arr, new_column):
    # Delete the second column
    arr_without_second_column = np.delete(arr, 1, axis=1)

    # Insert the new column in its place
    arr_without_second_column = np.insert(arr_without_second_column, 1, new_column, axis=1)

    return arr_without_second_column


# Example usage:
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

new_column = np.array([10, 11, 12])

result = delete_and_insert_column(arr, new_column)
print("Array after deleting the second column and inserting the new column:")
print(result)
