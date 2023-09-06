# 1. 나이 순으로 오름차순 정렬
# 2. 나이 같으면 먼저 가입한 순으로 정렬

li = []
i=0
import sys
n = int(input())
for _ in range(n):
    age, name = sys.stdin.readline().split()
    age=int(age)
    i+=1
    li.append([i, age, name])

for each in sorted(li, key= lambda x:(x[1], x[0])):
    print(each[1], each[2])