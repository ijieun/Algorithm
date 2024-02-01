# n과 m(12). start를 지정.
n,m = map(int, input().split())
li = list(map(int, input().split()))
ans = []
li.sort()
visited = [False]*n
def back(start):
    prev = 0
    if len(ans)==m:
        print(*ans)
        return
    else:
        for i in range(start,n):
            if prev != li[i]:
                ans.append(li[i])
                prev=li[i]
                back(i)
                ans.pop()
back(0)