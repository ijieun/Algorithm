n,m= map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
li = [ i for i in range(1,n+1)]

for i in range(m):
    st = grid[i][0]-1
    ed = grid[i][1]
    
    # [::-1]을 하면 손쉽게 역순으로 뒤집을 수 있음.
    li[st:ed]= li[st:ed][::-1]

for i in range(n):
    print(li[i], end=" ")