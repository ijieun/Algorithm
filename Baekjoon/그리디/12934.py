x, y = map(int, input().split())

if x == 0 and y == 0:
    print(0)
else:
    k = 1
    possible = True
    while True:
        # x와 y의 합이 1 ~ K까지의 합이라면 가능한 경우
        if x + y == k * (k + 1) // 2:
            break
        # 1 ~ K까지의 합이 아니라면 가능하지 않은 경우
        if x + y < k * (k + 1) // 2:
            possible = False
            break
        k += 1

    if not possible:
        print(-1)
    else:
        result = 0
        for i in range(k, 0, -1):
            if x == 0:
                break
            x -= min(x, i)
            result += 1
        print(result)
