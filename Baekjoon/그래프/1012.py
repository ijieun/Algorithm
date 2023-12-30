# bfs 배추심기
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [-1, 1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            
            if nx <0 or ny <0 or nx >= N or ny>=M:
                continue
            
            if matrix[nx][ny] ==1:
                queue.append((nx, ny))
                # 주변 1들을 0으로 바꿈
                matrix[nx][ny]=0
    return
                
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    
    for i in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
        
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j]==1:
                bfs(i, j)
                cnt += 1
print(cnt)