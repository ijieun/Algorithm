import sys
n=int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
for i in sorted(li):
    print(i)
# 파이썬 sys.stdin을 쓰는 방법