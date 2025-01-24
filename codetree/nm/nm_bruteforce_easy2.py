N = int(input())
A = list(map(int, input().split()))

# Write your code here!
count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1,N):
            if A[i]<=A[j]<=A[k]:
                # print(f"{A[i]}<={A[j]}<={A[k]}")
                count += 1
        
print(count)