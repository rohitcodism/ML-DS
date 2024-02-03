def baseCon(n, base):

    converted = []

    if n == 0:
         print("The result is  : ",0)
    else:
        while(n>0):
            rem = n%base
            converted.append(str(rem))
            n //=base
        print("The result is : ",''.join(converted[::-1]))

baseCon(23,2)