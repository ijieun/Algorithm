from collections import deque
t = int(input())


dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs(s_x, s_y):
    dq = deque()
    dq.append((s_x, s_y))
    visited[s_x][s_y] = 0

    while dq:
        x, y = dq.popleft()
        for i in range(8):
            n_x, n_y = x + dx[i], y + dy[i]
            if 0 <= n_x < n and 0 <= n_y < n:
                if visited[n_x][n_y] == -1:
                    visited[n_x][n_y] = visited[x][y] + 1
                    dq.append((n_x, n_y))

ans = []
for _ in range(t):
    n = int(input())
    x, y = tuple(map(int, input().split()))
    f_x, f_y = tuple(map(int, input().split()))
    visited = [[-1] * n for _ in range(n)]

    bfs(x, y)
    ans.append(visited[f_x][f_y])

for ele in ans:
    print(ele)
