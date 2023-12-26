import sys
input = sys.stdin.readline
n,m = map(int, input().split())

li = []
for i in range(1,n+1):
    li.append(i)
    
for i in range(m):
    one, two = map(int, input().split())
    li[one-1], li[two-1] = li[two-1], li[one-1]

for j in li:
    print(j,end=' ')