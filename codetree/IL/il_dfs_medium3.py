import sys 
n = int(input())
grid = [ list(map(int,input().split())) for _ in range(n) ]
visited = [[ False for _ in range(n)] for _ in range(n)]
pop_block_num = 0
block_num = 0
max_block_num = -sys.maxsize

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y, now_num):
    if not in_range(x,y):
        return False
    if visited[x][y]==True or grid[x][y]!= now_num:
        return False
    return True

def dfs(x,y, now_num):
    global pop_block_num
    global block_num
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(4):
        new_x = x + dxs[i]
        new_y = y + dys[i]
        if can_go(new_x, new_y, now_num):
            block_num += 1
            visited[new_x][new_y] = True
            dfs(new_x, new_y, now_num)
    

for i in range(n):
    for j in range(n):
        now_num=grid[i][j]
        if can_go(i,j, now_num):
            block_num = 1
            visited[i][j] = True
            dfs(i,j, now_num)
            if block_num >=4:
                pop_block_num += 1

        if block_num > max_block_num:
            max_block_num = block_num
        

print(pop_block_num, max_block_num)