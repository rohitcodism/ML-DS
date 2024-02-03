def move_duplicates_to_end(lst):
    unique_values = []
    duplicates = []

    # Separate unique values and duplicates
    for item in lst:
        if item not in unique_values:
            unique_values.append(item)
        else:
            duplicates.append(item)

    # Reconstruct the list with unique values followed by duplicates
    result = unique_values + duplicates

    return result


# Example usage
lst = [1, 2, 3, 4, 3, 5, 6, 1, 7, 8, 3, 9, 5]
result = move_duplicates_to_end(lst)
print("List after moving duplicates to end:", result)
