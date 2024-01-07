# max가 여러개면 여러개 출력됨.
# 중복 제거한 list에서 단어 개수 세리고, 새 list에 저장
# 새 list의 max index에 있는 원래 list위치 출력

import sys
input = sys.stdin.readline
s=input().strip()
s=s.upper()
li = list(set(s))
cnt =[]
for i in li:
    cnt.append(s.count(i))
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(li[cnt.index(max(cnt))])