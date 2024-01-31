n,m = map(int, input().split())
li = list(map(int, input().split()))
ans = []
li.sort()
visited = [False]*n
def back(start):
    prev = 0
    if len(ans)==m:
        print(" ".join(map(str, ans)))
        return
    else:
        for i in range(start,n):
            if prev != li[i] and visited[i]==False:
                ans.append(li[i])
                visited[i]=True
                prev=li[i]
                back(i)
                visited[i]=False
                ans.pop()
back(0)