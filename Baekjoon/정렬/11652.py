# 계수 정렬로 풀기
# 1. 입력받기
# 2. 해당 값에 있으면 위치에 +1씩 하기
# 3. max 값의 숫자를 출력
import sys
input = sys.stdin.readline
n = int(input())
arr = [0]*(n+1)

for _ in range(n):
    arr[int(input())] +=1

max_j=0
for _ in range(len(arr)):
    for j in arr:
        if j>max_j:
            max_j=j
        if j==max_j:
            max_j=min(j, max_j)
print(arr.index(max_j))