#problem 48
def euler48():
    x= sum(i**i for i in xrange(1,1000+1))
    return x % pow(10,10)

print euler48()

        
