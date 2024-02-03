def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_sequence(n):
    sequence_sum = 0
    for i in range(n+1):
        sequence_sum += 1 / factorial(i)
    return sequence_sum

# Example usage
n = int(input("Enter the value of n: "))
result = sum_sequence(n)
print("Sum of the sequence up to", n, "terms:", result)
