# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
n = int(input())
grid =[[ int(i) for i in map(str, input())] for _ in range(n) ]
visited = [[False for _ in range(n)] for _ in range(n)]
houseNumber = [[0 for _ in range(n)] for _ in range(n)]
houseCount = 0
houseCount_li = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]==True or grid[x][y]==0:
        return False
    return True

def dfs(x, y, index):
    global houseCount
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for i in range(4):
        new_x = x + dxs[i]
        new_y = y + dys[i]
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True 
            houseNumber[new_x][new_y] = index
            houseCount += 1 
            dfs(new_x, new_y, index)

index = 1
for i in range(n):
    for j in range(n):
        # 방문 안했을때 dfs 
        if grid[i][j] == 1 and visited[i][j]==False:
            # dfs 시작 전 count 를 1로 초기화 
            houseCount = 1
            visited[i][j] = True
            dfs(i, j, index)
            # 방문 가능할때 인덱스 1 추가, 리스트에 count 추가하기 
            index += 1 
            houseCount_li.append(houseCount)

# index 가 아니라 houseCount_li로 길이 출력하면 정답 
print(len(houseCount_li))
houseCount_li.sort()

for i in range(len(houseCount_li)):
    print(houseCount_li[i])