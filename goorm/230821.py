n = int(input())
s = input()
arr = []
for i in s:
	arr.append(i)

result = []
three_result=[]
for i in range(1,n + 1):
    for j in range(1,n + 1):
        for k in range(1,n + 1):
            if i + j + k == n:
                result.append(arr[:i])
                result.append(arr[i:i+j])
                result.append(arr[i+j:])
for i in range(0,len(result),3):
	three_result.append(result[i:i+3])
print('세개씩, three_result:',three_result)

unique_result = []

for i in result:
	if i not in unique_result:
		unique_result.append(i)

sorted_result = sorted(unique_result)
print('정렬 결과 점수, sorted_result:',sorted_result)

max_total = 0
for inner_list in three_result:
    sum_list = []
    for item in inner_list:
        s_item = "".join(item)
        for s_result in sorted_result:
            if s_item == "".join(s_result):
                index_sum = sorted_result.index(s_result) + 1
                sum_list.append(index_sum)
    
    if len(sum_list) >= 3:
        for i in range(len(sum_list) - 2):
            total = sum_list[i] + sum_list[i+1] + sum_list[i+2]
            max_total = max(max_total, total)

print(max_total)

