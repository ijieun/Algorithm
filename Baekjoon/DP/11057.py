n = int(input())
# 길이가 n인 오르막의 개수 구하기
# 0으로 시작할 수 있음

dp=[[0]*10 for _ in range(n+1)]
# # 0이 10개씩 n+1개 있음.
for i in range(10):
    dp[1][i]=1

# 핵심 아이디어
# => 그전 자리수로 이번의 자리수 경우의수를 알 수 있다.

for i in range(2,n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j]+=dp[i-1][k]

print(sum(dp[n])%10007)