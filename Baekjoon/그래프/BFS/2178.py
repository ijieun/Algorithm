from collections import deque
grid = []
min_go = 99999

n, m = map(int, input().split())
for i in range(n):
    input_str = input()
    grid.append([int(i) for i in input_str])


def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y]==0:
        return False
    return True 


go_count = 0
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs():
    global go_count, min_go, visited
    q = deque()
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    while q:
        x, y = q.popleft()

        for i in range(4):
            new_x = x + dxs[i]
            new_y = y + dys[i]

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append(new_x, new_y)
                go_count += 1
    min_go = min(min_go, go_count)
    go_count = min_go
    return go_count

bfs()
visited[0][0] = True
print(go_count)