from collections import deque

def in_range(x,y):
    global w, h 
    return 0<=x<h and 0<=y<w

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]==True or grid[x][y]==0:
        return False
    return True 

dxs, dys = [1,1,0,-1,-1,-1,0,1], [0,-1,-1,-1,0,1,1,1]

# bfs 로 풀기 
def bfs(r,c):
    # 한 번에 (r,c)라는 좌표 하나를 q에 넣어야함.
    q = deque([(r,c)])
    while q:
        cr,cc = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = cr+dx 
            new_y = cc+dy

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y)) 
    
while True:
    # 입력 받기 
    w, h = map(int, input().split())
    # 종료 조건 w,h 따로 주기 
    if w == 0 and h== 0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    result = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 1 and visited[r][c]==False:
                visited[r][c]=True
                bfs(r, c)
                result += 1

    print(result)