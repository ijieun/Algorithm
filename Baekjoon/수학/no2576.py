list = []

for i in range(7):
    num = int(input())
    if num%2 !=0:
        list.append(num)

if len(list)==0:
    print(-1)
else:
    print(sum(list))
    print(min(list))