def solution(prices):
    answer = []
    n=len(prices)
    # 전체 순회
    for i in range(n):
        c=0
        # i 이후, j 순회
        for j in range(i+1,n):
            # target보다 j가 더 작으면
            if prices[j]<prices[i]:
                # 1회 더하고 멈춤.
                c+=1
                break
            # 그렇지 않으면 계속 +1씩 더하기
            c+=1
        answer.append(c)
    return answer
print(solution([1, 2, 3, 2, 3]))
# [1, 2, 3, 2, 3]