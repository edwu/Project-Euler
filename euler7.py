#problem 7
def sieveOfEratosthenes():
    n=200000
    x=range(2,n)
    p=2
    while p**2<n:
        for a in x:
            if a == p:
                continue
            if a % p == 0:
                x.remove(a)
        p=x[x.index(p)+1]
    return x[10000]
print sieveOfEratosthenes()
    
