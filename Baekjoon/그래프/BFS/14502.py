from collections import deque
import copy

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# BFS 돌려서 바이러스 퍼뜨리기
def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y, temp_grid):
    if not in_range(x,y):
        return False
    if temp_grid[x][y]!=0:
        return False
    return True 

def bfs(temp_grid):
    cnt = 0
    q = deque()
    # 처음 바이러스 위치 전부 큐에 넣기
    for i in range(n):
        for j in range(m):
            if temp_grid[i][j] == 2:
                q.append((i, j))

    # 격자 탐색 
    dxs, dys=  [1,0,-1,0], [0,1,0,-1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + dxs[i]
            new_y = y + dys[i]

            if can_go(new_x, new_y, temp_grid):
                q.append((new_x, new_y))
                temp_grid[new_x][new_y] = 2
    # bfs 끝난 후 안전 영역 크기 리턴
    for i in range(len(temp_grid)):
        for j in range(len(temp_grid[i])):
            if temp_grid[i][j] ==0:
                cnt += 1

    return cnt 


max_safe = -9999999

# 세개의 서로 다른 벽 세우기 
empty_spaces = []  # 빈 공간 저장
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            empty_spaces.append((i, j))

# 빈 공간에서 3개의 벽 고르기 
for a in range(len(empty_spaces)):
    for b in range(a+1, len(empty_spaces)):
        for c in range(b+1, len(empty_spaces)):
            temp_grid = copy.deepcopy(grid)
            wall1 = empty_spaces[a]
            wall2 = empty_spaces[b]
            wall3 = empty_spaces[c]

            temp_grid[wall1[0]][wall1[1]] = 1
            temp_grid[wall2[0]][wall2[1]] = 1
            temp_grid[wall3[0]][wall3[1]] = 1

            safe_area = bfs(temp_grid)

            max_safe = max(max_safe, safe_area)
            
print(max_safe)
