import sys

n = int(input())
A = list(map(int, input().split()))
location = []
# Write your code here!

min_result = sys.maxsize
for index, people in enumerate(A):
    location.append((people, index))

# 0

for i in range(n):
    result = 0
    for people, index in location:
        result += people * abs(index-i)
    min_result = min(min_result, result)

print(min_result)