# (이면은 stack에 넣기.
# )이면은 pop하기.
# if pop할때 len이 0이면 print(NO)
# if 식이 다 돌았을때 stack에 남은게 있으면 print(NO)
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    stack = []
    vps = input()
    for i in vps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')