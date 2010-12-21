#problem 40

def euler40():
    c = "".join([str(x) for x in xrange(0,200000)])
    total = int(c[1]) * int(c[10]) * int(c[100]) * int(c[1000]) * int(c[10000]) * int(c[100000]) * int(c[1000000])
    return total

print euler40()
