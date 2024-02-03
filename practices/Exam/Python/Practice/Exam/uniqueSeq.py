def compute_sequence_sum(n):
    total_sum = 0
    numerator = 2
    denominator = 9
    sign = 1  # To alternate between positive and negative terms

    for i in range(n):
        term = sign * numerator / denominator
        total_sum += term

        # Update numerator and denominator for the next term
        numerator += 3
        denominator += 8
        sign *= -1  # Alternate sign for the next term

    return total_sum


# Example usage:
n_terms = int(
    input("Enter the number of terms: "))
sequence_sum = compute_sequence_sum(n_terms)
print("Sum of the sequence:", sequence_sum)
