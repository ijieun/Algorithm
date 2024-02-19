def solution(arr):
    answer = []
    stack=[]
    now_n = -1
    for i in arr:
        stack.append(i)
    while(len(stack)>0):
        pop_n = stack.pop()
        if pop_n != now_n:
            answer.append(pop_n)
            now_n = pop_n
    answer = answer[::-1]
    return answer
print(solution([5,4,34,3,4,4,8]))