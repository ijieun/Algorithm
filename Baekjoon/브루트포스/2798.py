# 블랙잭
# 앞에서부터 3개씩 무조건 더해보면서 m을 넘는지 확인.
# 만약 m을 안넘으면 더한 수에 m을 빼보고 이전 꺼보다 작은 수면 x를 치환
# 진짜 전부다 탐색해야 함.

import sys
input = sys.stdin.readline
n , m = map(int, input().split())
li = list(map(int, input().split()))
result=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                if li[i]+li[j]+li[k] <= m:
                    if li[i]+li[j]+li[k]>=result:
                        result = li[i]+li[j]+li[k]
print(result)