while True:
    a, b = map(int, input().split())
    if(0<a<10) & (0<b<10):
        print(a+b)
    if(a ==0 & b ==0):
        break