def reduce_string(s):
    stack = []

    for char in s:
        if stack and char == stack[-1]:
            stack.pop()  # Remove the matching adjacent character
        else:
            stack.append(
                char)  # Add the character to the stack

    result = ''.join(stack)
    return result if result else "Empty String"


# Example usage:
input_string = input(
    "Enter a string of lowercase characters: ")
reduced_string = reduce_string(input_string)
print("Reduced string:", reduced_string)
