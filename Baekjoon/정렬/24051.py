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
    # 리스트의 길이(n)를 구하고, 카운트(count)와 k_ 변수를 0으로 초기화/
    n = len(li)
    count = 0
    k_ = 0
    # 리스트의 두 번째 원소부터 마지막 원소까지 반복문을 돌며 각각에 대해 삽입 정렬을 수행
    for i in range(1,n):
        # 새로운 아이템(newItem)은 현재 인덱스 i의 값으로 설정하고, 위치(loc)은 i-1로 설정하여 이전 원소와 비교
        newItem = li[i]
        loc = i-1
        # 만약 위치가 0보다 크거나 같고 새 아이템이 현재 위치의 값보다 작으면
        while loc >= 0 and newItem < li[loc]:
            # 현재 위치+1에 현재 위치의 값을 복사하고 카운트를 하나 올림
            li[loc+1] = li[loc]
            count += 1
            # 그리고 위치를 하나 감소시키고 이 과정을 반복
            loc -= 1
            # 만약 카운트가 k와 같아지면, k_ 변수에 현재 위치+1 의 값을 저장
            if count == k:
                k_ = li[loc+1]
        # while 문 종료 후에 loc + 1 에 newItem 을 할당하여 실제로 해당 자리에 새로운 아이템을 넣음.
        li[loc+1] = newItem
        # 만약 loc + 1 가 i 와 같지 않다면(값이 이동되었으면) 카운트 하나 올림
        if loc + 1 != i:
            count += 1 
        # 카운트가 k 와 같아진 경우에도 k_ 변수 업데이트
        if count == k:
            k_ = li[loc+1]
    # 마지막으로 전체 for문 종료 후
    # 만약 k 가 count 보다 큰 경우 -1 출력
    if k>count:
        print(-1)
    # 그렇지 않다면, k_ 값을 출력
    else:
        print(k_)

insertion_sort(li)