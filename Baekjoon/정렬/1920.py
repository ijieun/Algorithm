# N에 M이 있는지 확인하기
# hashmap 생성해서 n에다가 key = count 로 수 저장. 없으면 0 저장
# 만약, m을 출력할때 hashmap에 있으면 1출력. 0이면 0출력
import sys
input = sys.stdin.readline
_ = int(input())
N=map(int, input().split())
_ = int(input())
M=map(int, input().split())
hashmap = {}

for n in N:
    if n in hashmap:
        hashmap[n]+=1
    else:
        hashmap[n]=1
for m in M:
    if m in hashmap:
        print(1)
    else:
        print(0)