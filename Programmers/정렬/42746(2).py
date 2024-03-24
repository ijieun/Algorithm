from functools import cmp_to_key
# cmp_to_key 사용!

def compare(x, y):
    # 나중에 들어온 요소가 앞으로 정렬됨 (뒤에거)
    if x+y > y+x:
        return 1
    # 바뀌지 않음
    elif x+y == y+x:
        return 0
    # 먼저 들어온 요소가 앞으로 정렬됨 (앞에거)
    else:
        return -1

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=cmp_to_key(compare),reverse=True)
    answer = str(int(''.join(n)))
    return answer