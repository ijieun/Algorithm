def solution(sizes):
    answer = 0
    large = []
    small = []
    
    for i in sizes:
        if i[0]>i[1]:
            large.append(i[0])
            small.append(i[1])
        else:
            large.append(i[1])
            small.append(i[0])

    answer = max(large)*max(small)
    return answer
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))