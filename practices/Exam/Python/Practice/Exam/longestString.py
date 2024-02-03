def longest_string_length(str_list):
    max_length = 0
    if len(str_list) > 0:
        for string in str_list:
            if len(string) > max_length:
                max_length = len(string)
        return max_length

# Example usage
str_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]
print("Length of the longest string:", longest_string_length(str_list))
