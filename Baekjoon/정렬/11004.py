import sys
input = sys.stdin.readline
n, k = input().split()
a = list(map(int, input().split()))
print(sorted(a)[int(k)-1])