def fibbonacci(n):
    fibo_series = [0,1]

    for i in range(2,n+1):
        next_term = fibo_series[-1] + fibo_series[-2]
        fibo_series.append(next_term)
    return fibo_series

print(fibbonacci(8))