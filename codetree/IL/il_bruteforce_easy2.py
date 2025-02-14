n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


seq_nums = [0 for _ in range(n)]

# 행복한 수열 판별 
def is_happy_sequence():
    consecutive_count, max_count=1, 1
    for i in range(1, n):
        if seq_nums[i-1] == seq_nums[i]:
            consecutive_count += 1 
        else:
            consecutive_count = 1 

        max_count = max(max_count, consecutive_count)

    return max_count >= m 

num_happy = 0

# 가로
for i in range(n):
    seq_nums = grid[i][:]

    if is_happy_sequence():
        num_happy += 1

# 세로
for j in range(n):
    # 세로 숫자들 모아서 새로운 수열 만들기 
    for i in range(n):
        seq_nums[i] = grid[i][j]

    if is_happy_sequence():
        num_happy += 1 

print(num_happy)