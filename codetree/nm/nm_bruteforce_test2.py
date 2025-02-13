arr = list(map(int, input().split()))

# Write your code here!
min_result = 9999999
total_sum = sum(arr)

for i in range(4):
    for j in range(i+1, 5):
        for k in range(5):
            fir_sum = 0
            if i==k or j==k:
                continue
            fir_sum += (arr[i]+arr[j])
            sec_sum = total_sum-fir_sum-arr[k]
            if fir_sum==sec_sum or sec_sum == arr[k] or \
                fir_sum == arr[k]:
                    continue
            else:
                min_sum = min(fir_sum, sec_sum, arr[k])
                max_sum = max(fir_sum, sec_sum, arr[k])

                min_result = min(min_result, abs(min_sum - max_sum))

if min_result == 9999999:
     print(-1)
else:
    print(min_result)