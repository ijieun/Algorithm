# if push면 두번째 인자를 append
# if top이면 len(li)의 li[수] 출력, 비었으면 0출력
# if size면 len(li)
# if empty면 if len이 0이면 1출력, 아니면 0 출력
# if pop이면 pop
import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    com = input().split()
    if com[0] == 'push':
        li.append(com[1])
    elif com[0] == 'top':
        if len(li)==0:
            print(-1)
        else:
            print(li[len(li)-1])
    elif com[0] == 'size':
        print(len(li))
    elif com[0] == 'empty':
        if len(li)==0:
            print(1)
        else:
            print(0)
    elif com[0] == 'pop':
        if len(li)==0:
            print(-1)
        else:
            print(li.pop())
    