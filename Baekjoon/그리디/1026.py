# a 는 오름차순 정렬
# b는 내림차순 정렬
# 두개 곱해서 합 구하기
import sys
input = sys.stdin.readline
n = int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
sum = 0
a.sort()
b.sort(reverse=True)
for i in range(n):
    sum += a[i]*b[i]
print(sum)