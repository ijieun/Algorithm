# 전위순회로 돌기x dfs로 풀기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

arr = []

def dfs(s):
    for i in graph[s]:
        if visited[i]==0:
            visited[i]=s
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])
