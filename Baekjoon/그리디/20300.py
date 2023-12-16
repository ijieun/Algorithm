import sys
input = sys.stdin.readline

n = int(input())
loss = list(map(int, input().split()))
loss.sort()

result = loss[-1]
if n%2 == 1:
    for i in range(n//2):
        tmp = loss[i]+loss[n-i-2]
        if result < tmp:
            result = tmp
elif n%2 == 0:
    for i in range(n//2):
        tmp = loss[i]+loss[n-i-1]
        if result < tmp:
            result = tmp
            
print(result)