d = int(input())
c = list(map(int, input().split()))
count = 0
for i in range(5):
    if(c[i]==d):
        count+=1
print(count)
# solved!!!