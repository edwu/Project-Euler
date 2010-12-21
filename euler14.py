#problem 14
def collatz(num):
    steps = 1
    while num != 1:
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        steps += 1
    return steps


def euler14(num):
    currentMax = 0
    maxIndex = 0
    for i in xrange(1,num):
        currentSteps = collatz(i)
        if currentSteps > currentMax:
            currentMax = currentSteps
            maxIndex = i
    return maxIndex
        
if __name__=="__main__":
    print euler14(1000000)



