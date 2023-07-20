n=int(input())
for i in range(0,n):
    print(' '*i+'*'*(n-i-1)*2+'*')
for i in range(1,n):
    print(' '*(n-i-1)+'*'*i*2+'*')
