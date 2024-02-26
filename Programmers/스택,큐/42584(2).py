from collections import deque
def solution(prices):
    answer = []
    prices=deque(prices)
    # 이중 반복문: while과 for 문 사용
    while prices:
        cnt = 0
        price = prices.popleft()
        for i in prices:
            cnt += 1
            if i<price:
                break
        answer.append(cnt)

    return answer
print(solution([1, 2, 3, 2, 3]))
