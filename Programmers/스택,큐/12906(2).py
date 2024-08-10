def solution(arr):
    answer = []
    answer.append(arr[0])
    now = arr[0]
    for i in range(len(arr)):      
        if now != arr[i]:
            now = arr[i]
            answer.append(now)
    return answer

print(solution([4,4,4,3,3]))