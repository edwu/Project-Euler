#problem 10

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

def sumPrimes(n):
    x=xrange(2,n)
    sum=0
    for num in x:
        if isPrime(num):
            sum+=num
    return sum

print sumPrimes(2000000)


