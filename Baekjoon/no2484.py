num = int(input())
diceList = []
for i in range(num):
    dice = list(map(int, input().split()))
    if(dice[0]==dice[1]==dice[2]==dice[3]):
        diceList.append(50000+dice[0]*5000)
    elif(dice[0]==dice[1] ==dice[2]):
        diceList.append(10000+dice[0]*1000)
    elif(dice[1]==dice[2] ==dice[3]):
        diceList.append(10000+dice[1]*1000)
    elif(dice[0]==dice[1] ==dice[3]):
        diceList.append(10000+dice[0]*1000)
    elif(dice[0]==dice[2] ==dice[3]):
        diceList.append(10000+dice[0]*1000)

    elif(dice[0]==dice[1] and  dice[2]!=dice[3]):
        diceList.append(1000+dice[0]*100)
    elif(dice[0]==dice[2]and dice[1]!=dice[3]) :
        diceList.append(1000+dice[0]*100)
    elif(dice[0]==dice[3] and dice[1]!=dice[2]):
        diceList.append(1000+dice[0]*100)
    elif(dice[1]==dice[2] and dice[0]!=dice[3]):
        diceList.append(1000+dice[1]*100)
    elif(dice[1]==dice[3] and dice[0]!=dice[2]):
        diceList.append(1000+dice[1]*100)
    elif(dice[2]==dice[3] and dice[1]!=dice[0]):
        diceList.append(1000+dice[2]*100)

    elif(dice[0]==dice[1]and dice[2]==dice[3]):
        diceList.append(2000+dice[0]*500+dice[2]*500)
    elif(dice[0]==dice[2]and dice[1]==dice[3]):
        diceList.append(2000+dice[0]*500+dice[1]*500)
    elif(dice[0]==dice[3]and dice[1]==dice[2]):
        diceList.append(2000+dice[0]*500+dice[1]*500)

    else:
        diceList.append(max(dice)*100)

print(max(diceList))