from collections import deque
import sys
input = sys.stdin.readline
graph_list ={}

n,m,v = map(int, input().split())
for _ in range(m):
    a, b = map(int,input().split())
    if a in graph_list:
        graph_list[a].append(b)
    else:
        graph_list[a]=[b]
    if b in graph_list:
        graph_list[b].append(a)
    else:
        graph_list[b]=[a]

def BFS_WITH_ADJ_LIST(graph, root):
    visited = []
    queue = deque([root])
    while queue:
        k = queue.popleft()
        if k not in visited:
            visited.append(k)
            if k in graph: # 추가된 부분
                queue += sorted( list(set(graph[k]) - set(visited)))
    return visited
print(BFS_WITH_ADJ_LIST(graph_list,v))