import sys
input = sys.stdin.readline
n=int(input())
count = 0

# 5로 계속 나누기
#그냥 거스름돈 안주고 제가 다 쓰면 안되나요? 
#네?
"""
    그냥 제가 다 쓸게요
    부자가 될게요
    자가를 사겠습니다.
"""
while (n > 0):  #n이 양수일때까지
    if n % 5 == 0:  #만약 n/5의 나머지가 0이면
        count += n //5
        break
    else:
        n -= 2  #만약 5로 안나눠지면 2로 뺌.그렇군요 이지니씨
        count += 1
        
if n < 0:
    print(-1)
else:
    print(count)