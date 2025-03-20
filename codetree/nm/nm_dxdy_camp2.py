li = list(input())
n = len(li)

def is_zero(x,y):
    return x ==0 and y ==0

count = 0
x, y = 0,0
dxs, dys = [0, 1,0,-1],[1,0,-1,0]
dir_n = 3
find_zero = False

for i in range(n):
    count += 1
    if li[i]=='L':
        dir_n = (dir_n+3)%4
    if li[i]=='R':
        dir_n = (dir_n+1)%4
    if li[i]=='F':
        nx = x + dxs[dir_n]
        ny = y + dys[dir_n]
    if is_zero(nx,ny):
        find_zero = True
        res = count 
        break
    x = nx
    y = ny
if find_zero:
    print(res)
else:
    print(-1)
    