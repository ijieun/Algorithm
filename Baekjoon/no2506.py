n = int(input())
s = list(map(int, input().split()))
stack=0
result=0
for i in range(n):
    if(s[i]==1):
        stack+=1
        result+=stack
    else:
        stack=0

print(result)
# read&solve