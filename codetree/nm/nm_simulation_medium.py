m1, d1, m2, d2 = map(int, input().split())
# 11 5 12 21

# Write your code here!

month = [0, 31, 28, 31,30,31,30,31,31,30,31,30,31]
# 1. 사이 달에 몇일 있는지 더하기
# 2. 해당 달에 몇일 있는지 빼기 (첫, 두)

result = 0

if m1 == m2:
    result = d2-d1 +1
else:
    result += month[m1] - d1 + 1 
    result += d2
    for i in range(m1+1, m2):
        result += month[i]

print(result)
