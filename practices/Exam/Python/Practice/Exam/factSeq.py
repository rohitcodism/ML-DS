def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def series_sum(x, n):
    sum = 0
    for i in range(1, n+1):
        term = (-1)**(i-1) * (x**i) / factorial(i)
        sum += term
    return sum

# Example usage
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms in the series: "))
result = series_sum(x, n)
print("Sum of the series:", result)
