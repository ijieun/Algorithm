import sys
input = sys.stdin.readline

N = int(input())
n_li = list(map(int, input().split()))
M = int(input())
m_li = list(map(int, input().split()))
hashmap= {}
for n in n_li:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1
for m in m_li:
    if m in hashmap:
        print(1, end=' ')
    else:
        print(0, end=' ')