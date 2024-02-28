def solution(numbers):
    numbers = list(map(str, numbers))
    # 자리수를 늘려서 비교 후 정렬
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    answer = ''.join(numbers)
    # 000인 경우에 0을 리턴
    if answer[0]=='0':
        return '0'
    else:
        return answer
print(solution( [979, 97, 978, 81, 818, 817]))