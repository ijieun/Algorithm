from collections import deque

n = int(input())
graph = [ [] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0] * (n+1)
visited= [False] * (n+1)

print(visited)
visited[1] = True
q = deque([1])
while q:
    node = q.popleft()
    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = node 
            q.append(nxt) 

for i in range(2, n+1):
    print(parent[i])
