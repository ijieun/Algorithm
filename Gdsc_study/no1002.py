import math

for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    #dis, 두 원의 중심 사이의 거리, 참고함
    dis = math.sqrt((x1-x2)**2 +(y1-y2)**2)

    #두 원의 중심이 같을 때
    if dis ==0:
        #반지름이 같을 때
        if r1==r2:
            print(-1)
        #반지름이 다를 때
        else:
            print(0)
    
    #두 원의 중심이 다를 때
    else:
        #외접이나 내접일 때
        if r1+r2 == dis or abs(r2-r1) ==dis:
            print(1)
        elif((abs(r1-r2)<dis) and (dis<r1+r2)):
            print(2)
        #그밖에 있을 때
        else:
            print(0)


