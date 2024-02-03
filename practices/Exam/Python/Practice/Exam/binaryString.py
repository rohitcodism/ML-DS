def isBinaryString(line):
    checker = [0,1]

    for char in line:
        if int(char) not in checker:
            return False
    return True

print(isBinaryString('10110010101'))