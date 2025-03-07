n = int(input())

li = [[0 for _ in range(220)] for _ in range(220)]

for i in range(n):
    x, y = map(int, input().split())
    for row in range(x, x+8):
        for col in range(y, y+8):
            li[row][col] = 1

cnt = 0
for row in range(-110, 110):
    for col in range(-110, 110):
        cnt += li[row][col]

print(cnt)