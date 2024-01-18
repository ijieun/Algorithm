import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A+B

answer = ' '.join(map(str, sorted(C)))
print(answer)