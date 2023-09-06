import sys
n=int(input())
list = []
for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    list.append([x,y])

for inner in sorted(list):
    for each in inner:
        print(each, end=' ')
    print('')