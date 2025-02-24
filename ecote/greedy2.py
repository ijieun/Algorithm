import sys

max_value = -sys.maxsize
n,m = map(int, input().split())


card = [
    list(map(int,input().split())) for _ in range(n)
    ]

for row in range(n):
    least = min(card[row])
    max_value = max(max_value, least)
print(max_value)