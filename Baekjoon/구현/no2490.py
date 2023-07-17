for i in range(3):
    count = 0
    play = list(map(int, input().split()))
    for j in play:
        if(j==0):
            count=count+1
    if(count==0):
        print('E')
    if(count==1):
        print('A')
    if(count==2):
        print('B')
    if(count==3):
        print('C')
    if(count==4):
        print('D')
    if(count==5):
        print('E')
# solved!!!