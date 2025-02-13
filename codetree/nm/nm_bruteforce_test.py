import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))

min_value = sys.maxsize

for i in range(N):
    for j in range(i+1, N):
        min_value = min(min_value, abs(S-(sum(arr)-arr[i]-arr[j])))

print(min_value)