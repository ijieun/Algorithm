def solution(n, lost, reserve):
    # n은 lost의 길이
    lostNum = len(lost)
    # 정렬
    lost = sorted(lost)
    reserve = sorted(reserve)

    # 만약 잃은 거랑 챙겨온 거랑 똑같은 숫자면 먼저 없앰.
    for i in range(len(lost)):
        print(lostNum, lost, reserve)
        for j in range(len(reserve)):
            if lost[i]==reserve[j]:
                lost[i]=-10
                reserve[j]=-10
                lostNum-=1
                print("챙겨온 애꺼 ",lostNum)

    # 챙겨온 애께 아니면 -1, +1 해서 확인.
    for i in range(len(lost)):
        print(lostNum, lost, reserve)
        for j in range(len(reserve)):
            if lost[i]-1==reserve[j]:
                print("%d가 안챙겨옴, 챙겨온 애 %d의 -1 애꺼 :"%(lost[i],reserve[j]) ,lostNum)
                lost[i]=-10
                reserve[j]= -10
                lostNum -= 1
            elif  lost[i]+1==reserve[j]:
                print("%d가 안챙겨옴, 챙겨온 애 %d의 +1 애꺼 :"%(lost[i],reserve[j])  ,lostNum)
                lost[i]=-10
                reserve[j]= -10
                lostNum -= 1


    return n-lostNum

# print(solution(5, [3, 4], [4, 3]))
# 기댓값: 5


# print(solution( 5, [1], [5]))
# # 기댓값: 4

# print(solution(5, [1, 4], [2, 4]))
# # 기댓값: 4
# print(solution( 5, [1, 2], [2, 3]))
# # 기댓값: 4

# print(solution(5, [2, 3, 5], [2, 3, 4]))
# # 기댓값: 5

# print(solution(30, [28, 30], [27, 29]))


