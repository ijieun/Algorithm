# deque 를 사용! 왼쪽 오른쪽 pop, append가 가능함.
from collections import deque

def solution(priorities, location):
    answer = 0
    deq_list = deque(priorities)
    while(True):
        pop = deq_list.popleft()
        
        # 만약 마지막 요소이면 답 반환
        if len(deq_list)==0:
            return answer+1 
        
        # 왼쪽 pop 한게 최대값보다 작으면 오른쪽에 다시 append 함
        if pop<max(deq_list):
            deq_list.append(pop)
        # pop한게 최대값이면 answer 1추가함. 이게 원하는 수였다면 답 반환
        else:
            answer += 1
            if location==0:
                return answer
        # 만약 location 위치가 0이었다면 끝 인덱스로 변경
        if location==0:
            location=len(deq_list)-1
        # 그렇지 않으면 인덱스 1 줄임
        else:
            location -=1