#problem 23
import math

def divisors(num):
    i = 1
    total = 0
    while i <= math.sqrt(num):
        if num % i == 0:
            total += i
            if num != i*i:
                total += num/i
        i += 1
    return total - num

def abundant(limit):
    listOfAbundant = [i for i in xrange(1,limit) if i < divisors(i)]
    return listOfAbundant

def sums(limit):
    abundantList = abundant(limit)
    listOfAbundant = []
    for i in abundantList:
        for j in abundantList:
            if i + j >= limit:
                break
            listOfAbundant.append(i+j)
    return set(listOfAbundant)

sumsOfAbundant = sums(28123)
total = 0
for x in xrange(1,28123):
    if x not in sumsOfAbundant:
        total += x
print total

