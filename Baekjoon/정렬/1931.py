# 핵심 아이디어: 끝나는 시간이 가장 빠른 것부터 출력
# 끝나는 시간이 빠른 것부터 정렬
# 만약 첫번째 수가 현재 두번째 수보다 크면 count +1
import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    s, e = map(int, input().split())
    li.append([s, e])
li.sort(key = lambda x :(x[1], x[0]))

now = 0
count = 0
for i in li:
    if i[0]>=now:
        count += 1
        now = i[1]
        
print(count)