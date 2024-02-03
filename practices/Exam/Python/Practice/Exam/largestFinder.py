def find_largest_and_second_largest(numbers):
    if len(numbers) < 2:
        print("At least two numbers are required.")
        return

    # Initialize variables to store the largest and second largest numbers
    largest = float('-inf')
    second_largest = float('-inf')

    # Iterate through the numbers to find the largest and second largest
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return largest, second_largest

# Input N numbers from the user
N = int(input("Enter the number of elements: "))
numbers = []

for i in range(N):
    num = float(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)

# Call the function to find the largest and second largest numbers
largest, second_largest = find_largest_and_second_largest(numbers)

# Print the results
print("Largest number:", largest)
print("Second largest number:", second_largest)
