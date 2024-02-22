from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리의 길이를 queue의 0으로 나타냄
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()
    
    # 남아있는 트럭이 있으면 반복
    while truck_weights:
        # 다리에서 왼쪽 트럭을 빼고 총 무게를 계산
        total_weight -= bridge.popleft()
        # 견딜수 있는 것보다 무거우면 0추가
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        # 현재 더 가벼우면 트럭하나를 추가
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            # 무게도 업데이트
            total_weight += truck
        # 시간 업데이트
        step += 1
    # 맨 마지막 트럭은 한 다리 길이만큼 시간 걸림. 시간 추가
    step += bridge_length

    return step
