# 1. 국어 점수 내림차순
# 2. 같으면, 영어 점수 오름차순
# 3. 같으면, 수학 점수 내림차순
# 4. 같으면, 이름이 사전순 증가
import sys
li = []
n = int(input())
for _ in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    li.append([name, int(kor), int(eng), int(math)])
for each in sorted(li, key =lambda x:(-x[1], x[2], -x[3], x[0])):
    print(each[0])