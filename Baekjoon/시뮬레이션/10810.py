n,m= map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
li = [ 0 for _ in range(n)]

for i in range(m):
    # for 반복문으로 시작과 끝 설정 
    for ch in range(grid[i][0]-1, grid[i][1]):
        li[ch] = grid[i][2]


for i in range(n):
    print(li[i], end=" ")