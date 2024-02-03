def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as file1:
        with open(output_file, 'w') as file2:
            # Iterate over each line in the input file
            for line_number, line in enumerate(file1, start=1):
                # Write the line number and the line content to the output file
                file2.write(f"{line_number}: {line}")

# Example usage:
input_file = "input.txt"
output_file = "output.txt"
add_line_numbers(input_file, output_file)
print("Line numbers have been added to the file.")
