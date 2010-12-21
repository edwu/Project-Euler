#problem 3
import math
def primeFinder(n):
    limit = math.sqrt(n)
    factors = [x for x in range(2,int(limit)) if n % x == 0]
    i,j=0,len(factors)-1
    while j>i:
        if factors[j] % factors[i] == 0:
            i,j=0,j-1
        else:
            i+=1
    print factors[j]

if __name__=="__main__":
    primeFinder(600851475143)
        

