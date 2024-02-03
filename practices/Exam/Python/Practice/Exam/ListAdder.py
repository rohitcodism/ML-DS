def add_lists(L, M):
    # Initialize the new list N
    N = []
    # Iterate over the elements of lists L and M simultaneously
    for i in range(len(L)):
        # Add the corresponding elements of L and M and append the sum to list N
        N.append(L[i] + M[i])
    return N

# Example usage
L = [3, 1, 4]
M = [1, 5, 9]

N = add_lists(L, M)
print("List N:", N)
