# 처음엔 최소 비용으로 이동한다음,
# 원래 비용보다 작으면 그대로 유지 & 2번 주유소에서 새로 주유.
# 원래 비용보다 크면 이전 주유소에서 가야할 거리만큼 더 플러스.

import sys
input = sys.stdin.readline
n = int(input())
dis=list(map(int, input().split()))
cost=list(map(int, input().split()))
result = 0

min_cost = cost[0]
for i in range(n-1):
    if cost[i]<min_cost:
        min_cost=cost[i]
        result += min_cost*dis[i]
    else:
        result += min_cost*dis[i]
# min cost 를 저장해두고, 비교하는 방법으로 수정.

print(result)