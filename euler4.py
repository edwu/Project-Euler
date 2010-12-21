#problem 4
def reverse(n):
    convert=str(n)
    i = len(convert)-1
    k=""
    while i>=0:
        k=k+convert[i]
        i=i-1
    return int(k)

def palindrome():
    arrayOfP=[]
    start=999
    i,j=start,start
    while i>99:
        while j>99:
            if i*j == reverse(j*i):
                arrayOfP=arrayOfP + [i*j]
            j=j-1
        start=start-1
        j=start
        i=i-1
    return arrayOfP


if __name__=="__main__":
    print max(palindrome())
