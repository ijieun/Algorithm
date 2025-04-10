from itertools import permutations

n, m = map(int, input().split())
ans = [i for i in range(1, n+1)]

for perm in permutations(ans, m):
    print(*perm)
