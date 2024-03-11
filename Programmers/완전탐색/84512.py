from itertools import product

def solution(word):
    target = ['A','E','I','O','U']
    arr = []
    # 1~5 길이의 중복 순열 생성(repeat 로 반복. product는 중복조합)
    for i in range(1,6):
        arr += list(map("".join, product(target, repeat=i)))

    # 정렬
    arr.sort()
    # 하나씩 돌면서 index 확인. word와 같으면 +1해서 리턴
    for i in range(len(arr)):
        if arr[i]==word:
            return i+1