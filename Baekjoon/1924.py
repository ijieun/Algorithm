x,y = map(int, input().split())

day=0
end_day=[31,28,31,30,31,30,31,31,30,31,30,31]
days=['SUN','MON','TUE','WED','THU','FRI','SAT']

for i in range(x-1):
    day+=end_day[i]
print(days[(day+y)%7])