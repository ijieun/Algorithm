import sys
input = sys.stdin.readline
n=int(input())
count = 0

# 5로 계속 나누기
while (n > 0):  #n이 양수일때까지
    if n % 5 == 0:  #만약 n/5의 나머지가 0이면
        count += n //5
        break
    else:
        n -= 2  #만약 5로 안나눠지면 2로 뺌.
        count += 1
        
if n < 0:
    print(-1)
else:
    print(count)