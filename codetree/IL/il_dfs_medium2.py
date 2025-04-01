import sys
sys.setrecursionlimit(2500)

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

zone_num = 0


# visited 배열을 초기화해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False


# 주어진 위치가 격자를 벗어나는지 여부를 반환합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 주어진 위치로 이동할 수 있는지 여부를 확인합니다.
def can_go(x, y, k):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] <= k:
        return False
    
    return True


def dfs(x, y, k):
    # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    # 네 방향에 각각에 대하여 DFS 탐색을 합니다.
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if can_go(new_x, new_y, k):
            visited[new_x][new_y] = True
            dfs(new_x, new_y, k)


def get_zone_num(k):
    global zone_num
    
    # 새로운 탐색을 시작한다는 의미로 zone_num를 0으로 갱신하고 
    # visited 배열을 초기화해줍니다.
    zone_num = 0
    initialize_visited()
    
    # 격자의 각 위치에 대하여 탐색을 시작할 수 있는 경우
    # 해당 위치로부터 시작한 DFS 탐색을 수행합니다.
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                # 해당 위치를 탐색할 수 있는 경우 visited 배열을 갱신하고
                # 안전 영역을 하나 추가해줍니다.
                visited[i][j] = True
                zone_num += 1
                
                dfs(i, j, k)


# 가능한 안전 영역의 최솟값이 0이므로 다음과 같이 초기화 해줄 수 있습니다.
max_zone_num = -1
answer_k = 0
max_height = 100

# 각 가능한 비의 높이에 대하여 안전 영역의 수를 탐색합니다.
for k in range(1, max_height +1):
    get_zone_num(k)
    
    # 기존의 최대 영역의 수보다 클 경우 이를 갱신하고 인덱스를 저장합니다.
    if zone_num > max_zone_num:
        max_zone_num, answer_k = zone_num, k

print(answer_k, max_zone_num)
