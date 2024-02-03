def is_ugly(num):
    if num <= 0:
        return False
    for prime in [2, 3, 5]:
        while num % prime == 0:
            num /= prime
    return num == 1

# Test cases
ugly_numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
for num in ugly_numbers:
    print(num, "is an ugly number:", is_ugly(num))
