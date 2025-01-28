R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]
# [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], 
# ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'],
#  ['W', 'W', 'W', 'W', 'B']]

print(grid)
count = 0

# 4중 for문

for i in range(R-1):
    for j in range(C-1):
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
                if grid[k][l]=="W":
                    if grid[k+1][l+1]=="B":
                        # if k==4 and l==4:
                        print(f"{ k , l } { k+1  ,l+1 }")
                        count+=1
                else:
                    if grid[k+1][l+1]=="W":
                            # if k==4 and l==4:
                        print(f"{ k , l } { k+1  ,l+1 }")
                        count+=1

# 한번 완주한 것임. 
print(count)
