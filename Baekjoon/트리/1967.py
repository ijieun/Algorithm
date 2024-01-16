# 트리 생성. dfs 두번 실행(임의의 노드에서 가장 먼 노드 구하기. 그 노드에서 가장 먼 노드 구하기.
# 그 노드의 거리를 구하기
# 풀이 참고o
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))
    
def DFS(node, cost):
    for adj_node, adj_w in tree[node]:
        cal_w = cost + adj_w
        if visited[adj_node] == -1:
            visited[adj_node] = cal_w
            DFS(adj_node, cal_w)
    
    return

# 첫번째 dfs: 지름의 양 끝점 중 하나 구하기
visited = [-1]*(n+1)
visited[1] = 0

DFS(1, 0)
idx, tmp = 0, 0
for i in range(1, len(visited)):
    if visited[i] > tmp:
        tmp = visited[i]
        idx = i

# 두번째 dfs: 나머지 트리의 지름 끝점 하나를 찾고 지름 구하기
visited = [-1]*(n+1)
visited[idx] = 0
DFS(idx, 0)

print(max(visited))