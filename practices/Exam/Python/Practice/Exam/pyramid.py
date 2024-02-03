def print_diamond_pattern(rows):
    # Upper half of the diamond
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")

        # Print numbers in increasing order
        for j in range(1, i + 1):
            print(j, end=" ")

        # Move to the next line for the next row
        print()

    # Lower half of the diamond (excluding the center row)
    for i in range(rows - 1, 0, -1):
        # Print leading spaces
        print(" " * (rows - i), end="")

        # Print numbers in increasing order
        for j in range(1, i + 1):
            print(j, end=" ")

        # Move to the next line for the next row
        print()


# Get the number of rows for the diamond from the user
rows = int(input("Enter the number of rows for the diamond: "))

# Call the function to print the diamond pattern
print_diamond_pattern(rows=7)
