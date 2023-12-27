# bfs 구현.
# 한번 함수 돌때 몇대가 바뀌는지 카운트 세기.
from collections import deque
n = int(input())
m = int(input())
graph = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1
    
visited = [False]*(n+1)


def bfs(v):
    counts =0
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for i in range(n+1):
            if not visited[i] and graph[v][i]==1:
                q.append(i)
                visited[i]=True
                counts +=1
    print(counts)
                
bfs(1)
