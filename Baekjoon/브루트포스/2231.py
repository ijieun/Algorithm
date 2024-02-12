# 생성자, 분해합 구하기
n = int(input())
for i in range(1, n+1):
    num = sum(map(int, str(i)))
    if i+num == n:
        print(i)
        break
else:
    print(0)