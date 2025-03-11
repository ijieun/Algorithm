n, t = tuple(map(int, input().split()))
x, y, c_dir = tuple(input().split())

# 각 알파벳 별 방향 번호를 설정합니다.
mapper = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3,
}
x, y, move_dir = int(x) - 1, int(y) - 1, mapper[c_dir]

dxs = [0, 1, 0, -1] 
dys = [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# simulation 진행
for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    # 범위 안에 들어온다면 그대로 진행합니다.
    if in_range(nx, ny):
        x, y = nx, ny
    # 벽에 부딪힌다면, 방향을 바꿔줍니다.
    else:
        move_dir = (move_dir +2) % 4

print(x + 1, y + 1)

