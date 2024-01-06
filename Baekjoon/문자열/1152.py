import sys
input = sys.stdin.readline
s = input().strip()
li = s.split(' ')
if li[0]=='':
    print(0)
else:
    print(len(li))