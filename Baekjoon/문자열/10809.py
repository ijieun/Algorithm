# find 사용법: s에 있는 i의 위치 찾기.
import sys
input = sys.stdin.readline
s= input()
a = "abcdefghijklmnopqrstuvwxyz"

for i in a:
    print(s.find(i), end=' ')