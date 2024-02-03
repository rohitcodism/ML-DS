import numpy as np
import random

randomMatt = [[random.randint(0,100)for _ in
              range(3)]for _ in range(3)]

for row in randomMatt:
    print(row)

def addition(randomatt):
    sumX = sum(randomatt[i][i] for i in range(3))
    print(sumX)
addition(randomMatt)