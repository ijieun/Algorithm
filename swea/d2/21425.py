t = int(input())

for i in range(t):
    a, b, n = map(int, input().split())
    x, y = min(a, b), max(a, b)
    count = 0
    # 둘다 n 이하면 반복
    while x <= n and y <= n:
        x, y = y, x + y
        count += 1

    print(count)

