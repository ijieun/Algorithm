def solution(participant, completion):
    dict = {}
    for i in participant:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for j in completion:
        if j in dict:
            dict[j] -= 1
    # 값이 1인것만 출력
    for key, value in dict.items():
        if value == 1:
            answer = key
    return answer
print(solution(["mislav", "stanko", "mislav", "ana","jini"], ["stanko", "ana", "mislav"]))