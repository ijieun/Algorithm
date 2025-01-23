n = int(input())  
sequence = list(map(int, input().split()))  

index = [(value, index) for index, value in enumerate(sequence)]

index.sort(key=lambda x: x[0])

result = [0] * n
for new_index, (value, original_index) in enumerate(index):
    result[original_index] = new_index + 1 

print(" ".join(map(str, result)))

