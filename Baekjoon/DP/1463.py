n=int(input())
dp=[0]*(n+1)
# dp 배열 생성

for i in range(2, n+1):
    # 1. 1을 빼는 경우
    dp[i]=dp[i-1]+1
    # 2. 만약, 2로 나누어 떨어질때 1을 빼는 경우와 2로 나누는 경우를 비교해서 최소값으로 지정
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)
    # 3. 위와 같이 3으로 나누어떨어지는 경우를 비교함, 최소 경우로 세팅.
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1)

# n인 경우의 연산 최솟값 출력
print(dp[n]) 