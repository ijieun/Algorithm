from collections import deque

def solution(priorities, location):
    answer = 0
    # 위치를 부여해줌
    data = deque(enumerate(priorities))
    while data:
        # data를 pop해서 검사
        l, priority = data.popleft()
        # 만약 data배열보다 pop한게 더 작으면 맨뒤에 다시 append
        if any(priority<p for _,p in data):
            data.append((l,priority))
        # pop한게 더 크면 answer +1. 그게 찾던 위치면 멈추고 출력
        else:
            answer += 1
            if l == location:
                break
    return answer
print(solution([2, 1, 3, 2], 3))