n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# [[1, 0, 1], [0, 1, 0], [0, 1, 0]]

MAX_VAL = -9999

for i in range(0, n-2):
    for j in range(0, n-2):
        sum_ = 0
        for k in range(3):
            for l in range(3):
                sum_ += int(grid[i+k][j+l])
        MAX_VAL = max(MAX_VAL, sum_)

print(MAX_VAL)