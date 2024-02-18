def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        # hash map 생성
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            # temp에서 비교 문자열 갱신 1 11 119...
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
print(solution(['127','1273','1232423','42342']))