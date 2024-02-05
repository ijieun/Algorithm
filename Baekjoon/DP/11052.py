# 점화식 (작은거부터 구하기)
# 2이면 1*2
# 3이면 p[3], p[1]+dp[2], p[2]+dp[1]
# ... 그래서 i부터 차례로 올라가면서 다 계산해보고 max값 구하기

n = int(input())
# 0을 추가해줘서 1부터 시작하도록. 더 쉽게 계산.
p = [0]+list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i], dp[i-j]+p[j])

print(dp[n])