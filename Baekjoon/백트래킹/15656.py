n, m = map(int, input().split())
li = list(map(int, input().split()))
ans = []
li.sort()
def back():
    if len(ans)==m:
        print(" ".join(map(str, ans)))
        return
    else:
        for i in li:
            ans.append(i)
            back()
            ans.pop()
back()