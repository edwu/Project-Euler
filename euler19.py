#problem 19

#def euler19():
months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def leapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def sundays(start,end):
    count = 0
    while start[2] < end[2]: #checks for the end of the year
        if leapYear(start[2]):
            months[2] = 29
        else:
            months[2] = 28
        start[1] += 7     #starts on a sunday increment by 7
        if start[1] > months[start[0]]:   #if the number of days is greater than the number of days in that month
            start[1] %= months[start[0]]
            start[0] += 1   #increase the month
        if start[0] > 12:  #if the number of months is greater than 12
            start[0] %= 12
            start[2] += 1  #increase the year
        if start[1] == 1:	#if sunday is 1st day of month
            count += 1
    return count

print sundays([1,6,1901],[1,1,2001])

