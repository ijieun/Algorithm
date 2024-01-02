# 오름차순 정렬
# 배열을 돌면서 sum에 저장.
# 그 저장한걸 다 더하기.
import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
sum = 0
result=0
sorted_li = sorted(li)
for i in sorted_li:
    sum+=i
    result += sum
print(result)