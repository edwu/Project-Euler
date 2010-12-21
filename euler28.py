#problem 28
def euler28(num):
    rowcount,start,total = 1,1,1
    start = 1
    currentIncrement=2
    rowCount = 2
    k = 0
    while rowCount <= num:
        while k < 4:
            print start
            start += currentIncrement
            total += start
            k += 1
        k = 0
        currentIncrement += 2
        rowCount += 1
    return total
print euler28(501)

#this represents the number of layers 
            
        
        
