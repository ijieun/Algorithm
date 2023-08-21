n = int(input())
s = input()
arr = []
for i in s:
	arr.append(i)

result = []
for i in range(1,n + 1):
    for j in range(1,n + 1):
        for k in range(1,n + 1):
            if i + j + k == n:
                result.append([arr[:i], arr[i:i+j], arr[i+j:]])

								
# print('만들 수 있는 모든 배열: result',result)

unique_list = []
for sub_list in result:
    for item in sub_list:
          if item not in unique_list:
                unique_list.append(item)
                unique_list.sort()

# print(unique_list)
# 중복 제거하고 sort

sum_list = []

for sub_list in result:
    for item in sub_list:
        if item in unique_list:
            index = unique_list.index(item)
            sum_list.append(index+1)

# print("result2의 인덱스가 더해진 sum_list:", sum_list)

grouped_sums = [sum(sum_list[i:i+3]) for i in range(0, len(sum_list), 3)]
max_sum = max(grouped_sums)

print(max_sum)