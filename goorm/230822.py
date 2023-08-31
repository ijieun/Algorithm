n, k = map(int, input().split())
d = [0] * n
# list 초기값 생성하면서 깃발 정보 입력받기
for l in range(n):
    d[l] = list(map(int, input().strip().split()))

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

count_map = [[0] * n for _ in range(n)]

# 깃발 순회하기
for i in range(n):
    for j in range(n):
        if d[i][j] == 1:
            for d_i, d_j in directions:
                x, y = i + d_i, j + d_j

                # 인덱스가 리스트 범위 내에 있는지 확인
                # 깃발 있는 자리에서는 카운트 증가X
                if 0 <= x < n and 0 <= y < n and d[x][y] != 1:
                    count_map[x][y] += 1

count = 0
# 결과 출력
for row in count_map:
    for inner in row:
        if inner == k:
            count += 1
print(count)