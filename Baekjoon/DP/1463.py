n = int(input())
dp = [0]*(n+1)

for i in range(2,n+1):
    # 일단 1을 빼는 경우로 최솟값 세팅
    dp[i]=dp[i-1]+1

    # 2로 나누어 떨어지는 경우 체크
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)

    # 3으로 나누어 떨어지는 경우 체크
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
print(dp[n])
    