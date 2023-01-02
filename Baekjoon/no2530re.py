h, m, s = map(int, input().split())
sec = int(input())

# 최종 초
s1=(s+sec)%60
s=(s+sec)//60

# 최종 분
m1=(m+s)&60

# 최종 시

print(h,m,s)
