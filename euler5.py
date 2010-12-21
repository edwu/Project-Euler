def diviser(n):
    i = 1
    while i<=20:
        if n % i != 0:
            return False
        i+=1
    return True

def smallest():
    i=1
    while (1):
        if diviser(i):
            return i
        i+=1
    return "Never Reaches Here"
k=smallest()
print k
