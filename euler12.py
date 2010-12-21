#problem 12

def genTriangleNums(limit):
    i = 2
    triangles = [1]
    while i < limit+2:
        if i-1 == len(triangles):
            yield triangles[i-2]
            triangles.append(i+triangles[i-2])
        i+=1

def findFactors(num):
    i = 1.0
    count = 0
    while i <= num/i:
        if i == num/i:
            return count*2+1
        if num % i == 0.0:
            count+=1
        i+=1
    return count * 2

def numOfDivisors(divisors,limit):
    for num in genTriangleNums(limit):
        if findFactors(num)>=divisors:
            return num
    return "No number with this many divisors with this limit."

print numOfDivisors(500,100000000)


