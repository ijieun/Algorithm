# 큐는 선입 선출, 먼저 들어간게 먼저 나온다.
import sys
input=sys.stdin.readline
n=int(input())
queue=[]
for i in range(n):
    m=input().split()
    if m[0]=='push':
        queue.append(int(m[1]))
    elif m[0]=='pop':
        if queue:
            print(queue[0])
            del(queue[0])
        else:
            print(-1)
    elif m[0]=='size':
        print(len(queue))
    elif m[0]=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif m[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif m[0]=='back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)
