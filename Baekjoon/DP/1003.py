import sys
input = sys.stdin.readline
zero = [1,0,1]
one = [0,1,1]
def fibonacci(n):
    length = len(zero)
    if n > length:
        for i in range(length,n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])
        
t = int(input())
# dp에는 0과 1의 호출횟수 저장

for _ in range(t):
    n = int(input())
    fibonacci(n)