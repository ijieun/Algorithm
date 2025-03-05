h, m = map(int, input().split())
h2, m2 = map(int, input().split())

cnt = 0
while True:
    if h == h2 and m == m2:
        break
    m += 1 
    cnt += 1 

    if m==60:
        h += 1
        m = 0
    

print(cnt)