import sys
input = sys.stdin.readline
li=[]
n = int(input())
for i in range(n):
    num = int(input())
    li.append(num)
for i in sorted(li):
    print(i)