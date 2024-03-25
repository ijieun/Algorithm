def solution(clothes):
    dict = {}
    # 0은 곱하기 불가
    answer = 1
    for clothe in clothes:
        kind = clothe[1]
        if kind in dict:
            dict[kind] += 1       
        else:
            # 옷을 입는경우, 안입는 경우
            dict[kind] = 2
    for i in dict.values():
        # 전체 value끼리 곱해서 경우의 수 생성.
        answer *= i
    # 전체 다 안입는 경우는 빼기
    return answer - 1
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])