import sys
sys.setrecursionlimit(10**7)

t = int(input())

def in_range(x,y):
    # x가 행, y가 열 역할 
    return 0<= x < n and 0<= y < m

def can_go(x,y):
    if not in_range(x,y):
        return False 
    if visited[x][y] == True or grid[x][y] ==0:
        return False 
    return True 

# def initialize():
#     for i in range(m):
#         for j in range(n):
#             visited[i][j] = False
#             grid[i][j] = 0


def dfs(x,y):
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    for i in range(4):
        new_x = x + dxs[i]
        new_y = y + dys[i]

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True 
            dfs(new_x, new_y)
        

for i in range(t):
    m, n, k = map(int, input().split())
    grid =[ [0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0 


    for j in range(k):
        x, y = map(int, input().split())
        # grid에 x, y 가로 세로 위치 조정 
        grid[y][x] = 1

    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1 and visited[x][y]==False:
                visited[x][y] = True
                count += 1 
                dfs(x,y)
    print(count)
