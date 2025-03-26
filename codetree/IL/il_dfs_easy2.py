# 격자에서 DFS !!!!

n,m = map(int, input().split())

# 뱀 위치 이중 배열 
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 방문 리스트
visited =[ [0 for _ in range(m)] for _ in range(n) ]

def in_range(x,y):
    return 0<= x and x<n and 0<=y and y<m

def can_go(x,y):
    if not in_range(x,y):
        return 0
    if visited[x][y] or grid[x][y]==0:
        return 0
    return 1

# dfs 돌리기 
def dfs(x,y):
    dxs, dys = [1,0], [0,1]
    for i in range(2):
        new_x = x +dxs[i]
        new_y = y+ dys[i]
        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            # 재귀 
            dfs(new_x, new_y)

dfs(0,0)
visited[0][0] = 1
# visited 에서 n,m 번째 이중 배열 바로 출력 
# 0은 False, 1은 True 인 사실을 이용 
print(visited[n-1][m-1])