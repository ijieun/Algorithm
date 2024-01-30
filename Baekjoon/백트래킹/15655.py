# n과m(6) - 리스트 안에서 돌고, start를 갱신하고, 0에서 시작하도록 수정.
n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
ans = []
def back(start):
    if len(ans)==m:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, n):
        if li[i] not in ans:
            ans.append(li[i])
            back(i)
            ans.pop() #return 으로 돌아오면 실행됨.
back(0)