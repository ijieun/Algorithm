import sys
n = int(input())
a = [int(input()) for _ in range(n)]
# [4, 7, 8, 6, 4]

min_value = sys.maxsize

# i에서 시작해서
for i in range(n):
    value = 0
    # j까지 감 
    for j in range(n):
        # 원형 거리 계산 !!
        dist = (j+n-i) % n 
        value += dist * a[j]
    min_value = min(min_value, value)

print(min_value)