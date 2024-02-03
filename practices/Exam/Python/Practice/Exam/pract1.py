#  # problem 1
#
# s = input("Enter any word with more than 2 letter : ")
# print("The user input string is : "+s)
#
# s.strip()
#
# print(s[1:-1])



# # problem 2
#
# s1 = input("Enter first word with more than 2 letter : ")
# s2 = input("Enter second word with more than 2 letter : ")
#
# l1 = len(s1)
# l2 = len(s2)
#
# s3 = s1[0] + s1[l1//2] + s1[-1] + s2[0] + s2[l2//2] + s2[-1]
#
# print(s3)



# # problem 3
#
# s1 = input("Enter first word with more than 2 letter : ")
# s2 = input("Enter second word with more than 2 letter : ")
#
# l1 = len(s1)
# middle1 = l1//2+1
#
# s3 = s1[0:middle1] + s2 + s1[middle1:]
# print(s3)