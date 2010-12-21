#problem 9
def pythagorean():
    a,b,c=1,1,1
    while a<1000:
        while b<1000:            
            c=1000-a-b
            if a**2+b**2==c**2:       
                if a+b+c == 1000:
                    return a*b*c
            b+=1
        a+=1
        b=0
print pythagorean()
