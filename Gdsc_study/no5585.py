a = 1000 - int(input())
b = [500,100,50,10,5,1]
# 거스름돈 개수, count=0
count = 0
for i in b:
    # 거스름돈 개수 = 낼 수 있는 동전의 개수 count = count + a//i
    count += a//i
    # 나머지 내야하는 금액 a = a%i
    a %= i 
print(count)

# read&sovled