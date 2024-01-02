# 잔돈을 계속 교체.
# 500이상이면 500으로 나누기. 빼서 교체.
# 500미만 100이상이면 100으로 나누기. 빼서 교체. 몫은 카운트에 초과.
import sys
input = sys.stdin.readline
n = 1000-int(input())
cnt =0
if n>=500:
    cnt += n//500
    n-= 500*(n//500)
if 500>n>=100:
    cnt += n//100
    n-= 100*(n//100)
if 100>n>=50:
    cnt += n//50
    n-= 50*(n//50)
if 50>n>=10:
    cnt += n//10
    n-= 10*(n//10)
if 10>n>=5:
    cnt += n//5
    n-= 5*(n//5)
if 5>n>=1:
    cnt += n//1
    n-= 1*(n//1)
print(cnt)