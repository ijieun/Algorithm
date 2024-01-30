# n과m(8)
# 이전 수와 같은지, 방문했는지 판별해서 ans에 추가
n,m = map(int,input().split())
li = list(map(int,input().split()))
ans = []
li.sort()
prev = 0
visited = [False]*n
def back(start):
    prev = 0
    if len(ans)==m:
        print(" ".join(map(str, ans)))
        return
    else:
        for i in range(n):
            if li[i] != prev and visited[i]==False:
                ans.append(li[i])
                prev = li[i]
                visited[i]=True
                back(i)
                ans.pop()
                visited[i]=False
back(0)
