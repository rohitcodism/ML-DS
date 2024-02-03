def kth_largest_factor(N, k):
    factors = []  # List to store factors of N

    # Iterate through numbers from 1 to N
    # for i in range(1, N + 1):
    #     if N % i == 0:  # Check if i is a factor of N
    #         factors.append(i)  # Add i to the list of factors
    i = N

    while N > 0 and i > 0:
        if N % i == 0:
            factors.append(i)
        i -= 1

    print(factors)

    if k > len(factors):  # Check if k is greater than the number of factors
        return None  # Return None if k is greater than the number of factors

    return factors[k-1]  # Return the kth largest factor of N


# Example usage:
N = int(input("Enter a positive integer N: "))
k = int(input("Enter the value of k: "))

kth_largest_factor_N = kth_largest_factor(N, k)
if kth_largest_factor_N is not None:
    print(f"The {k}th largest factor of {N} is: {kth_largest_factor_N}")
else:
    print(f"There are fewer than {k} factors for {N}.")
