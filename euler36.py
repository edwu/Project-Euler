#problem 36

def isPalindrome(num):
    str1 = str(num)
    str2 = str1[::-1]
    return str1 == str2
        
def dToB(num):
    binary = ""
    if num == 0:
        return '0'
    while num > 0:
        binary = str(num % 2) + binary
        num = num >> 1
    return int(binary)

def euler36():
    return sum(x for x in xrange(0,1000000) if isPalindrome(x) and isPalindrome(dToB(x)))

print euler36()

