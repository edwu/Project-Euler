#problem 21
import math
#def euler21():

def divisors(num):
    i = 1
    total = 0
    while i <= math.sqrt(num):
        if num % i == 0:
            total += i
            total += num/i
        i += 1
    return total - num

def euler21(limit):
    sum = 0
    for i in xrange(limit):
        a = divisors(i)
        b = divisors(a)
        if a != b and i == b:
            sum += i
    return sum

print euler21(10000)
