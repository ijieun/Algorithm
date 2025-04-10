n = int(input())
customer = list(map(int, input().split()))
senior_c, junior_c = map(int,input().split())

def count_junior(num):
    junior_cnt = 0
    if num <= 0:
        junior_cnt = 0
    elif (num % junior_c) ==0:
        junior_cnt += (num // junior_c)
    else:
        junior_cnt += (num // junior_c) + 1
    return junior_cnt

ans = 0
for i in range(n):
    ans += 1 
    ans += count_junior(customer[i]-senior_c)

print(ans)