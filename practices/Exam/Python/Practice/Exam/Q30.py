# Simple Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
else:
    print("Invalid input")

# Compare two equal-sized lists
def find_difference(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return i
    return "Lists are identical"

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 4, 4, 5]
difference_index = find_difference(list1, list2)
print("\nIndex where the lists differ:", difference_index)

# Reverse a list without using another list or in-built function
def reverse_list(lst):
    start_index = 0
    end_index = len(lst) - 1
    while start_index < end_index:
        lst[start_index], lst[end_index] = lst[end_index], lst[start_index]
        start_index += 1
        end_index -= 1

my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print("\nReversed list:", my_list)
