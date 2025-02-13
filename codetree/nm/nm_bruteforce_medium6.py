abilities = list(map(int, input().split()))

# Write your code here!

min_minus = 9999

for i in range(len(abilities)):
    for j in range(i, len(abilities)):
        all_sum = sum(abilities)
        for k in range(j, len(abilities)):
            fir_sum = abilities[i]+abilities[j]+abilities[k]
            all_sum -= fir_sum
            minus = abs(fir_sum-all_sum)

            min_minus = min(min_minus, minus)

print(min_minus)