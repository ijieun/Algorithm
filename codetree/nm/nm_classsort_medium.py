n = int(input())
# 4
# 1 8
# 3 4
# 5 5
# -7 0
points = [(int(i)+1, tuple(map(int, input().split()))) for i in range(n)]
# [(0, (1, 8)), (1, (3, 4)), (2, (5, 5)), (3, (-7, 0))]
# Write your code here!


# 1. 원점에서 가까운 순 -> 원점으로부터 거리 계산
# 2. 거리 짧은 순 출력 -> 번호 작은 순 출력 

points.sort(key = lambda x: (abs(x[1][0]+x[1][1]), x[0]))

for num in points:
    print(num)