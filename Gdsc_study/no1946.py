t =int(input())
for i in range(t):
    n =int(input())
    for j in range(n):
        people_list = [0]*n
        a, b = input().split()
        # a는 서류심사 성적 순위, b는 면접 성적의 순위
        a = int(a)
        b = int(b)
