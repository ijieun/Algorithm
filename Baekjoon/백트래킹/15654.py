n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
ans = []
def back():
    if len(ans)==m:
        print(" ".join(map(str, ans)))
        return
    for i in li:
        if i not in ans:
            ans.append(i)
            back()
            ans.pop() #return 으로 돌아오면 실행됨.
back()