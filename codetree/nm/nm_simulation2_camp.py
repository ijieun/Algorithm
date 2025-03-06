n = list(input())
dx = [1,0,-1,0]
dy = [0,-1,0,1]
dir_num=3
x,y= 0,0
for i in range(len(n)):
    if n[i]=='L':
        dir_num = (dir_num+3)%4
    if n[i]=='R':
        dir_num = (dir_num+1)%4

    if n[i]=='F':
        x += dx[dir_num]
        y += dy[dir_num]

print(x,y)