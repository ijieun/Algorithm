m1, d1, m2, d2 = map(int, input().split())

# Write your code here!

month_in_day = [0, 31, 28, 31,30,31,30,31,31,30,31,30,31]
week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
reverse_week = ['Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']

def find_remain_day(m1, d1, m2, d2):
    remain_day = 0
    if m1==m2:
        if d1>d2:
            remain_day = d2 - d1 
        else:
            remain_day = d2 - d1
    elif m1>m2:
        for i in range(m2+1, m1):
            remain_day += month_in_day[i]
        remain_day += d1
        remain_day += month_in_day[m2] - d2 -1

    else:
        for i in range(m1+1, m2):
            remain_day += month_in_day[i]
        remain_day += month_in_day[m1] - d1
        remain_day += d2 

    return remain_day

def find_what_day(remain_day):
    remain_day = remain_day % 7
    if remain_day < 7 and m1>m2:
        return reverse_week[remain_day]
    elif remain_day < 7:
        return week[remain_day]

print(find_what_day(find_remain_day(m1, d1, m2, d2)))
