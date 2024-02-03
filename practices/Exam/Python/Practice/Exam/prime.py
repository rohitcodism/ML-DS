def isPalindrome(num):
    return str(num) == str(num)[::-1]

def isPrime(num):
    if num<2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def checkTwoFact(num):
    if isPalindrome(num) and isPrime(num):
        return num

start = int(input("Enter the starting point : "))

end = int(input("Enter the end point : "))

checked = []

for i in range(start,end+1):
    res = checkTwoFact(num=i)
    if res != None:
        checked.append(res)

print(checked)