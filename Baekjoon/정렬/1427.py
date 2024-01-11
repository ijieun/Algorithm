import sys
input = sys.stdin.readline
n = int(input())
li = []

for i in str(n):
    li.append(i)
li.sort(reverse=True)
for i in li:
    print(i, end='')
