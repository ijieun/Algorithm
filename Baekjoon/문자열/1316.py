# 이전에 나왔던 단어냐?
# yes: 바로 이전 단어랑 똑같은 거냐?
#     yes: 굿
#     no: 멈춤
# no: 굿
# + li를 비우고 멈춤. li 가 비었으면 count 추가x. 안비었으면 count 추가o.
import sys
input = sys.stdin.readline
count =0
n = int(input())
for i in range(n):
    li = []
    s = input()
    for i in range(len(s)):
        # yes
        if s[i] in li:
            # yes
            if s[i] == s[i-1]:
                continue
            # no
            else:
                li = []        
                break
        # no
        else:
            li.append(s[i])
    if li:
        count+=1
print(count)