import sys
input = sys.stdin.readline
e, s, m = map(int, input().split())
# 15, 28, 19
# 만약, e는 15 이하인데 s는 16 이상or e과 다른수, m은 16 이상or e와 다른수면
# 1에서부터 e,s,m이 1,2,3이 될때까지 반복
a, b, c, result = 0,0,0,0

# 다 같은 수면 그대로 e 출력
while True:
    a +=1
    b+=1
    c+=1
    result +=1
    if a>15:
        a -= 15
    if b>28:
        b-= 28
    if c>19:
        c-=19
    if a==e and b == s and c == m:
        print(result)
        break