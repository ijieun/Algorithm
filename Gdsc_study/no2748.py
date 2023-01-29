n=int(input())
l = [0,1]

for i in range(1,n+1):
    new = l[len(l)-1]+l[len(l)-2]
    l.append(new)

print(l[n])