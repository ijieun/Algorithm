n=int(input())
for i in range(n):
    if i==0:
        print(' '*(n-i-1) + '*')
    elif i==(n-1):
        print('*'*(n-1)*2+'*')
    else:
        print(' '*(n-i-1)+'*'+' '*(i-1)*2+ ' '+'*')
