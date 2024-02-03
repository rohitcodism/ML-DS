def display_max_min(lst, start_index, end_index):
    if start_index < 0 or end_index >= len(lst):
        print("Error: Index out of range.")
        return

    sublist = lst[start_index:end_index + 1]
    max_val = max(sublist)
    min_val = min(sublist)

    print("List:", lst)
    print("Range of indexes:", start_index, "to", end_index)
    print("Maximum value:", max_val)
    print("Minimum value:", min_val)

# Example usage
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

display_max_min(my_list, start_index, end_index)
