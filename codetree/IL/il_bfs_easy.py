from collections import deque
n, k = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
k_list = [list(map(int, input().split())) for _ in range(k)]
visited = [[False for _ in range(n)] for _ in range(n)]
visited_count = k
q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<n 

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]==True or n_list[x][y]==1:
        return False
    return True 

def bfs():
    global visited_count
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
   
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True
                visited_count += 1 

for i in range(k):
    visited[k_list[i][0]-1][k_list[i][1]-1] = True    
    q.append((k_list[i][0]-1, k_list[i][1]-1))
bfs()

print(visited_count)