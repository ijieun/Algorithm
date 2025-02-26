import sys
n = int(input())
arr = [0] + list(map(int, input().split()))
# 4 -1 2 -19 3 6 9

min_value = -sys.maxsize
dp = [0]*(n+1)

def init():
    for i in range(1, n+1):
        dp[i] = min_value
    dp[1] = arr[1]

init()
for i in range(2, n+1):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

ans = min_value
for i in range(1, n+1):
    ans = max(ans, dp[i])

print(ans)