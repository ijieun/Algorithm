# 크거나 같음. 주의!
import sys
input = sys.stdin.readline
n, k =map(int, input().split())
li=[]
for i in range(n):
    a= int(input())
    li.append(a)
li.sort(reverse=True)
cnt =0
for j in li:
    if j<=k:
        cnt+=k//j
        k -= (k//j)*j
print(cnt)        
