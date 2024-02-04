n = int(input())
# 크기가 n인 직사각형을 채우는 방법의 수
# 어느정도 점화식 노가다 필요
dp = [0]*1001
dp[1]=1
dp[2]=3
for i in range(3,n+1):
    dp[i]=dp[i-1]+2*dp[i-2]
print(dp[i]%10007) 