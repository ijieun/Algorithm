# n과m(8)
n,m = map(int,input().split())
li = list(map(int,input().split()))
ans = []
li.sort()
def back(start):
    if len(ans)==m:
        print(" ".join(map(str, ans)))
        return
    else:
        for i in range(start, n):
            ans.append(li[i])
            back(i)
            ans.pop()
back(0)