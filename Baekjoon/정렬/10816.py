# 파이썬 hashmap = dictionary
# hashmap 에 해당값 없으면 값 추가. 있으면 그 값에 더하기
# 그냥 정렬은 시간복잡도 초과. hashmap 으로 구현.
import sys
input = sys.stdin.readline
_ = int(input())
N=map(int, input().split())
_ = int(input())
M=map(int, input().split())
hashmap = {}

for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1
print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))