#problem 20

def sumFactorial(n):
    currentFactorial = 1
    i=1
    while i <= n:
        currentFactorial *= i
        i += 1
    return currentFactorial

print sum(int(i) for i in str(sumFactorial(100)))
