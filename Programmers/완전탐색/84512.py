from itertools import product

def solution(word):
    target = ['A','E','I','O','U']
    arr = []
    # 1~5 길이의 중복 순열 생성
    for i in range(1,6):
        arr += list(map("".join, product(target, repeat=i)))

    arr.sort()
    # 하나씩 돌면서 index 확인
    for i in range(len(arr)):
        if arr[i]==word:
            return i+1