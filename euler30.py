#problem 30
def euler30():
    answer = 0
    i = 2
    while i < 500000:
        total = 0
        for k in range(0,len(str(i))):
            total += int(str(i)[k])**5
        if total == i:
            answer += i
        i += 1
    return answer
print euler30()
