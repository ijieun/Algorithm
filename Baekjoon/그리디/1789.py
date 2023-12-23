# s에서 1에서 증가하는 수로 차례로 뺌. 
# 만약, 빼는 수가 i보다 커지면 멈추고 출력
import sys
input = sys.stdin.readline
s = int(input().rstrip())
for i in range(1,s+1):
    if s<i:
        print(i-1)
        break
    if s==1:
        print(1)
    s-=i