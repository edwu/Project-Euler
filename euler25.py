#problem 25
def euler25(num=1,num2=1,limit=1000):
    fib,i=0,2
    while len(str(fib)) < limit:
        fib = num + num2
        num2 = num
        num = fib
        i += 1
    return i
        

print euler25()
