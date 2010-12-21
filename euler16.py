#problem 16
def sumOfDigits(num):
    summation = sum(int(i) for i in str(2**num))
    return summation
    
print sumOfDigits(1000)
        
