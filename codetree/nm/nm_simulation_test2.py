n = int(input())
li = [0 for _ in range(2100)]
now = 0

for i in range(n):
    x, dir = map(str, input().split())
    x = int(x)
    if dir == 'L':
        for j in range(now-x, now):
            li[j] += 1
        now = now-x
    if dir == 'R':
        for j in range(now, now+x):
            li[j] += 1
        now = now+x

cnt = 0
for i in range(-1000,1100):
    if li[i] >= 2:
        cnt += 1
print(cnt)