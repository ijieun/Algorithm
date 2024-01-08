import sys
input = sys.stdin.readline
s = input().strip()
li = []
r_li = []

for i in range(len(s)-1,-1,-1):
    r_li.append(s[i])
for i in s:
    li.append(i)
if r_li == li:
    print(1)
else:
    print(0)