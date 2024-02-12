def solution(participant, completion):
    dict = {}
    
    answer = list(set(participant) - set(completion))
    return answer
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))