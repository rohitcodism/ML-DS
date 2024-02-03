def contains_all_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # Convert the input string to lowercase
    s_lower = s.lower()
    # Check if all vowels are present in the string
    return all(vowel in s_lower for vowel in vowels)

# Example usage:
input_string = input("Enter a string: ")
if contains_all_vowels(input_string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
