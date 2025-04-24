import sys
sys.setrecursionlimit(10**7)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
max_safe_zone = -999999

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]==True or grid[x][y]<=h:
        return False
    return True 

# 영역 물들이기 
def dfs(x,y):
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    for dx, dy in zip(dxs, dys):
        new_x = x + dx 
        new_y = y + dy 
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y)

def initialize():
    global safe_zone
    safe_zone = 0
    for r in range(n):
        for c in range(n):
            visited[r][c] = False
            

# 아예 비가 오지 않는 경우인 0도 포함해줘야 함. 
for h in range(0, 101):
    initialize()
    for r in range(n):
        for c in range(n):
            # 안전 영역 찾기 
            if grid[r][c] > h and visited[r][c]==False:
                visited[r][c] = True 
                dfs(r, c)

                # 물에 안젖은 영역 카운트 1 추가 
                safe_zone += 1

    # 최대 안전영역 수 결론내리기 
    max_safe_zone = max(max_safe_zone, safe_zone)

print(max_safe_zone)