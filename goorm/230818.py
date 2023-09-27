n, k = map(int, input().split())
a = list(map(int, input().split()))
newArr = []

for i in a:
	binary_num = bin(i)[2:]
	count = 0
	for j in binary_num:
		if(j == '1'):
			count = count+1
	newArr.append([count, i])
	
newArr.sort(reverse = True)
print(newArr[k-1][1])
