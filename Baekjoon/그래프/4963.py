# 위 아래 대각선을 1로 생성했다가 0으로 바꿔서
# dfs 를 할 때마다 count 1씩 추가
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x,y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    field[x][y]=0
    q = deque()
    q.append([x,y])
    
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx <0 or ny < 0 or nx >=h or ny >=w:
                continue
            if field[nx][ny]==1:
                field[nx][ny]=0
                q.append([nx,ny])
    
# 0. 입력
while True:
    w, h = map(int, input().split())
    # field = [[0]*w for _ in range(h)]
    
    if w==0 and h==0:
        break
    # 입력받을때 개수에 한계X
    field = []
    cnt = 0
    for _ in range(h):
        field.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if field[i][j]==1:
                bfs(i,j)
                cnt +=1
    print(cnt)

            