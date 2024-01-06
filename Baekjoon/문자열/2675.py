import sys
input = sys.stdin.readline
t=int(input())
for i in range(t):
    n,s=input().split()
    n=int(n)
    for j in s:
        print(j*n, end='')
    print()