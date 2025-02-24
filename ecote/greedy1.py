# 가장 큰 수 번갈아서 계속 더해서 최대값 출력하기 
n,m,k = map(int, input().split())

num = list(map(int, input().split()))
num.sort(reverse=True)

result = 0
count = 0
for i in range(m):
    plus = num[0]
    count += 1
    if count >= k:
        if plus == num[0]:
            plus = num[1]
        else:
            plus = num[0]
        count = 0
    result += plus

print(result)