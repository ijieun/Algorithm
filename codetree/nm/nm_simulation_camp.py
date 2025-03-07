OFFSET = 1000
MAX_R = 2000

# 변수 선언 및 입력
n = 2
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    # OFFSET을 더해줍니다.
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    
    # 직사각형에 주어진 순으로 1, 2 번호를 붙여줍니다.
    # 격자 단위로 진행하는 문제이므로
    # x2, y2에 등호가 들어가지 않음에 유의합니다.
    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] = i

# 1, 2 순으로 붙였는데도
# 아직 숫자 1로 남아있는 곳들 중 최대 최소 x, y 값을 전부 계산합니다.
min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0
first_rect_exist = False
for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if checked[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

# 넓이를 계산합니다.
# Case 1. 첫 번째 직사각형이 전혀 남아있지 않다면 넓이는 0입니다.
if not first_rect_exist:
    area = 0
# Case 2. 첫 번째 직사각형이 남아있다면, 넓이를 계산합니다.
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)
