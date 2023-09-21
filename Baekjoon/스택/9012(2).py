# 1. 입력 다 받기
# 2. 괄호를 하나씩 다 잘라서 돌기
# 3. 만약, 괄호가 (이면 push
# 4. 만약, 괄호가 )이면 pop
# pop할때 stack 안에 없으면 no
# 다 끝냈을때, stack 이 비었으면 yes
# stack에 남아있으면 no


import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    g = input()
    stack = []
    for i in g:
        if i=='(':
            stack.append(i)
        elif i==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break;
    else:
        if not stack:
            print('YES')
        else:
            print('NO')

