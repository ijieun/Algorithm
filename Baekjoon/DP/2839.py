import sys
input = sys.stdin.readline
n = int(input())
dp = [-1]*5001
dp[3]=1
dp[5]=1
for i in range(6,n+1):
    if i%5 == 0:
        dp[i]=dp[i-5]+1
    elif i%3 == 0:
        dp[i]=dp[i-3]+1
    elif dp[i-3]>0 and dp[i-5]>0:
        dp[i]=min(dp[i-3], dp[i-5])+1
print(dp[n])
# https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-2839%EB%B2%88-%EC%84%A4%ED%83%95-%EB%B0%B0%EB%8B%ACdppython