def lcm(a,b):
    return (a*b)/gcd(a,b)

def gcd(a,b):
    r=0
    while(b!=0):
        r= a%b
        a=b
        b=r
    return a

for i in range(int(input())):
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(round(lcm(a,b)))
