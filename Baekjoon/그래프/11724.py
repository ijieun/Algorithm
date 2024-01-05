# 방향 없는 그래프. graph 생성할때, 정보 생성할때 주의

import sys
sys.setrecursionlimit(10**7)
# 0. 입력 및 초기화
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[False] for _ in range(n+1)]
visited = [False]*(n+1)

# 1. graph 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    # graph[u][v] = True
    # graph[v][u] = True
    graph[u].append(v)
    graph[v].append(u)
    

# 2. dfs     
def dfs(idx):
    global visited
    visited[idx] = True
    for i in graph[idx]:
        if visited[i]==False:
            visited[i] = True
            dfs(i)
count =0       
for i in range(1, n+1):
    if visited[i] == False:
        count += 1
        dfs(i)
        
print(count)