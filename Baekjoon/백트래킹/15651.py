n,m = map(int, input().split())
ans = []

def back():
    if len(ans)==m:
        print(" ".join(map(str, ans)))
    else:
        for i in range(1, n+1):
            # if i not in ans:
            ans.append(i)
            back()
            ans.pop()

back()