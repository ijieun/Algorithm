N = int(input())
a = []
for i in range(N):
    M = int(input())
    a.append(M)
    
a.sort(reverse=True)
b = []
for j in range(N):
    b.append(a[j]*(j+1))

print(max(b))