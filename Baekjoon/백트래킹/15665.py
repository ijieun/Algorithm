# 정렬 다른데 ok?
# 이전에 방문했던 거 재방문 가능. 이전 숫자와 같은지만 확인
n,m = map(int, input().split())
li = list(map(int, input().split()))
ans = []
li.sort()
real_ans = []
def back(start):
    prev = 0
    if len(ans)==m:
        print(*ans)
        return
    else:
        for i in range(n):
            if prev != li[i] :
                ans.append(li[i])
                prev=li[i]
                back(i)
                ans.pop()
back(0)
