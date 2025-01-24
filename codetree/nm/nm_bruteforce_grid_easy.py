n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# [[1, 0, 1], [0, 1, 0], [0, 0, 0]]
# Write your code here!


max_count = 0
for i in range(n):
    for j in range(n-2):
        max_count = max(max_count, grid[i][j]+grid[i][j+1]+grid[i][j+2])

print(max_count)