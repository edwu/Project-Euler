#problem 37
def truncL(num):
    sn = str(num)
    for i in xrange(len(sn)-1):
        sn = sn[1:]
        yield sn

def truncR(num):
    sn = str(num)
    k=len(sn)
    for i in xrange(k):
        sn = sn[:k]
        k -= 1
        yield sn

def isPrime(n):
    if n == 1:
        return 0
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

def truncate(num):
    for i in truncR(num):
        if isPrime(int(i)):
            continue
        else:
            return False
    for j in truncL(num):
        if isPrime(int(j)):
            continue
        else: 
            return False
    return True

def euler37():
    return sum(i for i in xrange(10,1000000) if truncate(i))

print euler37()
        
