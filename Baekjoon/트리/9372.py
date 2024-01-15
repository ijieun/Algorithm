# 1~n를 다 들리는 최소 개수 구하기 : n-1번
# 엔터 많이 되어도, 마지막 입력값에 붙어 있어도 ok
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    for j in range(m):
        a,b = map(int, input().split())
    print(n-1)
