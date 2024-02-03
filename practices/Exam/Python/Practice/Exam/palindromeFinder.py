def isPalindrome(num):

    num_str = str(num)
    return num_str == num_str[::-1]

def findPalindrome(num_arr):
    palindrome = []

    for num in num_arr:
        if isPalindrome(num):
            palindrome.append(num)
    print(palindrome)

findPalindrome([123, 151, 321, 474])