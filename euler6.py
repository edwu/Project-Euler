#problem 6
def sumOfSquares():
    i=1
    total=0
    while i<=100:
        total+=i**2
        i+=1
    return total
def squareOfSum():
    i=1
    total = 0
    while i<=100:
        total += i
        i+=1
    return total**2

print squareOfSum()-sumOfSquares()

#this method eliminates redundant squaring and subtracting
def simplified():
    total=0
    i,j=1,1
    while i <=100:
        while j<=100:
            if i==j:
                j+=1
                continue
            total+=i*j
            j+=1
        j=1
        i+=1
    return total
print simplified()
