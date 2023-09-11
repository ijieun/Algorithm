import sys
input = sys.stdin.readline
n, k = input().split()
for _ in range(int(n)):
    a = list(map(input().split()))
print(sorted(int(a))[int(k)])