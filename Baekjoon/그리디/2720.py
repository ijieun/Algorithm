# 돈을 쿼터에서부터 몫을 구해서 돈을 치환하고, 돈의 거스름돈을 출력.
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    c = int(input())
    q = c//25
    c -= (c//25)*25
    d = c//10
    c -= (c//10)*10
    n = c//5
    c -= (c//5)*5
    print(q,d,n,c)
    