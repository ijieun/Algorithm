# 백준: 알고리즘 수업-삽입 정렬1
# newItem: 정렬되지 않는 부분에서 첫번째 원소(현재 정렬 대상인 원소)
# loc: newItem이 삽입될 위치를 찾기 위해 사용되는 변수
# count: 현재 저장 횟수
# k_: k번째 저장되는 원소 (출력하기 위함)
import sys
input = sys.stdin.readline
a, k = map(int, input().split())
li= list(map(int, input().split()))

def insertion_sort(li):
    n = len(li)
    count = 0
    k_ = 0
    for i in range(1,n):
        newItem = li[i]
        loc = i-1
        while loc >= 0 and newItem < li[loc]:
            li[loc+1] = li[loc]
            count += 1
            if count == k:
                k_ = li[loc+1]
            loc -= 1

        li[loc+1] = newItem
        if loc + 1 != i:
            count += 1 
        if count == k:
            k_ = li[loc+1]

    if k>count:
        print(-1)
    else:
        print(k_)

insertion_sort(li)