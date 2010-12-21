#problem34
def factorial(n):
    i = 1
    total = 1
    if n == 0:
        return total
    while i <= n:
        total *= i
        i += 1
    return total

def factorial_array():
    factArray = []
    for i in xrange(0,10):
        factArray.append(factorial(i))
    return factArray

def euler34():
    factArray = factorial_array()
    i = 3
    total = 0
    while i < 50000:
        temp = 0
        for k in range(0,len(str(i))):
            temp += factArray[int(str(i)[k])]
        if temp == i:
            total += i
        temp = 0
        i += 1
    return total
print euler34()
