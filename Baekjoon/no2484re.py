N = int(input())
money_list=[]
for _ in range(N):
    lst = sorted(list(map(int, input().split())))
    if len(set(lst))==1:
        money_list.append(lst[0]*5000+50000)
    if len(set(lst))==2:
        if lst[1]==lst[2]:
            money_list.append(lst[1]*1000+10000)
        else:
            money_list.append((lst[1]+lst[2])*500+2000)
    for i in range(3):
        if lst[i]==lst[i+1]:
            money_list.append(lst[i]*100+1000)
    if len(set(lst))==4:
        money_list.append(lst[-1]*100)

print(max(money_list))