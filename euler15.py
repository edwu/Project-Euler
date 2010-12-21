#problem 15

def embeddedArray(grid):
    a = []
    for i in xrange(grid):
        a.append([])
        for j in xrange(grid):
            a[i].append(0)
    x,y=grid-1,grid-1
    while y >= 0:
        while x >= 0:
            if x == grid-1 and y == grid-1:
                a[y][x]=1
            else:
                if y == grid-1:
                    a[y][x]=a[y][x+1]
                elif x == grid-1:
                    a[y][x]=a[y+1][x]
                else:
                    a[y][x]=a[y][x+1]+a[y+1][x]
            x -= 1
        x=grid-1
        y -= 1
    return a[0][0]
print embeddedArray(21)

