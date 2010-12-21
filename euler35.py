#problem 35
def euler35():
    x = [i for i in xrange(2,1000000) if isCircularPrime(i)]
    return len(x)

def isCircularPrime(num):
    i = 0
    while i < len(str(num)):
        if (isPrime(int(num))):
            num = rotate(str(num))
            i += 1
            continue
        else:
            return False
    return True

def rotate(num):
    if len(num) == 1:
        return num
    rotated = num[1:] + num[:1]
    return rotated

def isPrime(n):
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    max = n**0.5 + 1
    i = 3
    while i <= max:
        if n % i == 0:
            return 0
        i+=2
    return 1

print euler35()




