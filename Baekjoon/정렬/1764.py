# 해쉬맵을 이용해서 단어 있는지 확인

import sys
input = sys.stdin.readline
N = []
M = []
answer = []
hashmap = {}

n,m = map(int, input().split())
for i in range(n):
    N.append(input())
for i in range(m):
    M.append(input())
    
for i in N:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1
for i in M:
    if i in hashmap:
        answer.append(i)
print(len(answer))
for i in sorted(answer):
    print(i, end='')