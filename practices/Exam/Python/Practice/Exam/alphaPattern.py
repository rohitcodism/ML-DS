def print_pattern(rows):
    for i in range(rows):  # Outer loop for rows
        char = 'A'  # Start with character 'A'
        for j in range(i + 1):  # Inner loop for printing characters in each row
            print(char, end=" ")
            char = chr(ord(char) + 1)  # Increment character for the next iteration
        print()  # Move to the next line for the next row

# Example usage:
rows = int(input("Enter the number of rows for the pattern: "))
print("Pattern:")
print_pattern(rows)
