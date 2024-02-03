def findPrimeFax(num):

    fax = []

    while num % 2 == 0:
        fax.append(2)
        num //= 2
    for i in range(3, int(num**0.5)+1, 2):
        while num % i == 0:
            fax.append(i)
            num //= i
    if num > 2:
        fax.append(num)
    print(fax)

findPrimeFax(60)