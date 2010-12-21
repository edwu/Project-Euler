#2 puzzle
limit=4000000

def generator(x,y):
    total = 0
    if x >= limit:
        return total
    if x%2==0:
        total += x
    return generator(y,x+y)

if __name__=="__main__":
    z= generator(0,1)
    print z









