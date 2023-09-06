# 1. y좌표가 증가하도록 정렬
# 2. y좌표가 같으면 x 좌표 큰거 우선 정렬

import sys
li = []
n = int(input())
for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    li.append([x,y])
for inner in sorted(li, key= lambda x: (x[1], x[0])):
    for each in inner:
        print(each, end=' ')
    print('')