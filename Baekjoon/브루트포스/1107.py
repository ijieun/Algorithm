# 완전 탐색으로 풀기
# 단순한듯 구현 어려운 문제
target = int(input())
ans = abs(100-target)

M = int(input())
if M:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001):
    for N in str(num):
        if N in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)