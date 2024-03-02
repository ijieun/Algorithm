def solution(answers):
    answer = []
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1, c2, c3 = 0,0,0

    for i in range(len(answers)):
        if answers[i] == m1[i%len(m1)]:
            c1 += 1
        if answers[i] == m2[i%len(m2)]:
            c2 += 1
        if answers[i] == m3[i%len(m3)]:
            c3 += 1

    value = max(c1, c2, c3)
    if c1 == value:
        answer.append(1)
    if c2 == value:
        answer.append(2)
    if c3 == value:
        answer.append(3)
                
    # a = 'You can do it '
    # b = 'im not gonna lie youre the best '

    # print(a + "\n" + b)

    return answer
print(solution([1,3,2,4,2]))