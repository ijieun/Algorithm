import sys
input = sys.stdin.readline
s = input().rstrip()
        
one=0
zero=0

now = s[0]
if now == "0": 
    zero +=1
else:
    one +=1

for i in range(1,len(s)):
    if s[i] != now:
        if s[i] == "0":
            zero +=1
            now = '0'
        else:
            one+=1
            now='1'

print(min(zero,one))