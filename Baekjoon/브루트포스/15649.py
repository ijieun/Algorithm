# 백트래킹 n과m(1)
n, m = map(int, input().split())
ans = []

def back():
    if len(ans)==m:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            back()
            ans.pop() #return 으로 돌아오면 실행됨.
back()