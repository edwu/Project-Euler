#problem 17
def total(num):
    nums=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    hundreds=["","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred","sevenhundred","eighthundred","ninehundred"]
    if num < 20:
        return len(nums[num])
    elif num < 100:
        return len(tens[num/10])+total(num%10)
    elif num < 1000:
        if num % 100 == 0:
            return len(hundreds[num/100])+total(num%100)
        else: 
            return len(hundreds[num/100])+len("and") + total(num%100)
    elif num==1000:
        return len("onethousand")
print sum(total(i) for i in xrange(1,1001))

