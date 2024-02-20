def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)>0:
        if(progresses[0]+speeds[0]*time>=100):
            progresses.pop()
            speeds.pop()
            count +=1
        else:
            if count>0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
print(solution([90,90], [10,9]))
