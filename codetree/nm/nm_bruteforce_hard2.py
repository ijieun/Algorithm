# 변수 선언 및 입력
n = int(input())
arr = [
	int(input())
	for _ in range(n)
]

# 모든 쌍을 다 잡아봅니다.
ans = -1
for i in range(n):
	for j in range(i + 1, n):
		for k in range(j + 1, n):
			carry = False
			
			# 일의 자리에서 carry가 발생하는 경우
			if arr[i] % 10 + arr[j] % 10 + arr[k] % 10 >= 10:
				carry = True
			
			# 십의 자리에서 carry가 발생하는 경우
			if arr[i] % 100 // 10 + arr[j] % 100 // 10 + arr[k] % 100 // 10 >= 10:
				carry = True
			
			# 백의 자리에서 carry가 발생하는 경우
			if arr[i] % 1000 // 100 + arr[j] % 1000 // 100 + arr[k] % 1000 // 100 >= 10:
				carry = True
			
			# 천의 자리에서 carry가 발생하는 경우
			if arr[i] % 10000 // 1000 + arr[j] % 10000 // 1000 + arr[k] % 10000 // 1000 >= 10:
				carry = True
			
			if carry == False:
				ans = max(ans, arr[i] + arr[j] + arr[k]);

print(ans)
