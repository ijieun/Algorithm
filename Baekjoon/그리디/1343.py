import sys
input = sys.stdin.readline
s=input().rstrip()

new_li=[]
li = s.split('.')
for i in li:
    if len(i)%2==0:
        if len(i)==2:
            new_li.append('BB')
        else:    
            a_count=(4*(len(i)//4))
            b_count=len(i)-a_count
            new_li.append(a_count*'A'+b_count*'B')
    else:
        new_li=[]
        print(-1)
        break
print('.'.join(new_li))