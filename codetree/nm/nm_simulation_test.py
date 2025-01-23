m1, d1, m2, d2 = map(int, input().split())
A = input()

# Write your code here!

week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

def num_of_days(m,d):
    month_in_day = [0, 31, 29, 31,30,31,30,31,31,30,31,30,31]
    day = 0
    for i in range(m):
        day += month_in_day[i]
    day += d
    return day

count = (num_of_days(m2,d2) - num_of_days(m1,d1)) // 7
remain = (num_of_days(m2,d2) - num_of_days(m1,d1)) % 7

for i in range(remain):
    if week[i]=="A":
        count += 1 

print(count)