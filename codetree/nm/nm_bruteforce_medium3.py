n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# [(0, 0), (8, 3), (11, -1), (10, 0)]
x = [p[0] for p in points]
# [0, 8, 11, 10]
y = [p[1] for p in points]
# [0, 3, -1, 0]

import sys

def min_distance(n):
    min_value = sys.maxsize

    for i in range(1,n-1):
        li = points[0:i]+points[i+1:]
        value = 0
        for j in range(len(li)-1):
            value += abs(li[j][0]-li[j+1][0]) + abs(li[j][1]-li[j+1][1])

        min_value = min(min_value, value)
    return min_value


print(min_distance(n))