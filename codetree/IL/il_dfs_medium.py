# 격자에서 DFS, 근데 이중 for문 + dx dy 탐색 

n = int(input())
# 전체 판 : grid
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
# 방문했는지 판별 : visited 배열 
visited = [[0 for _ in range(n)] for _ in range(n)]
people_num = 0
people_num_li = []

def in_range(x,y):
    return 0<=x and x <n and 0<=y and y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]==1 or grid[x][y]==0:
        return False
    return True 

def dfs(x,y):
    global people_num

    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    for i in range(4):
        new_x = x+dxs[i]
        new_y = y+dys[i]

        if can_go(new_x, new_y):
            visited[new_x][new_y]=1
            people_num += 1
            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if can_go(i,j):
            visited[i][j] = 1 
            people_num = 1

            dfs(i, j)

            people_num_li.append(people_num)

people_num_li.sort()

print(len(people_num_li))

for i in range(len(people_num_li)):
    print(people_num_li[i])