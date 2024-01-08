# 단어의 len을 같이 저장 [len, 단어]
# sort시킴. 출력.
import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    s = input().strip()
    li.append([len(s), s])

print_li= []
for i in sorted(li):
    if i[1] in print_li:
        continue
    else:
        print_li.append(i[1])
        print(i[1])