def find_max_min_with_indices(lst):
    if not lst:
        return None, None, None, None

    max_value = max(lst)
    min_value = min(lst)
    max_index = lst.index(max_value)
    min_index = lst.index(min_value)

    return max_value, max_index, min_value, min_index


# Example list
numbers = [5, 8, 2, 10, 3, 7]

# Call the function to find max and min values along with their indices
max_value, max_index, min_value, min_index = find_max_min_with_indices(numbers)

# Print the results
print("Maximum value:", max_value, "at index:", max_index)
print("Minimum value:", min_value, "at index:", min_index)
