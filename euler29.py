#problem 29
def euler29():
    x = (i**j for i in xrange(2,101) for j in xrange(2,101))
    return len(set(x))
print euler29()
