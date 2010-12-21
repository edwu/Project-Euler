#problem 22

names = open('names.txt').read().replace('"', '').split(',')
names.sort()

def nameTotal(name):
    return sum(ord(i)-ord("@") for i in name)
    
        
print sum((i+1)*nameTotal(names[i]) for i in xrange(0,len(names)))
    
