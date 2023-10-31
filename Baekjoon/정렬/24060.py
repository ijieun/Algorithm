def merge_sort(A, p, r): #p가 시작, r이 마지막
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q ,r): # q는 p와 r의 사이
    tmp = []
    i = p # i는 왼쪽 첫번째 값
    j = q + 1 # j는 오른족 첫번째 값

    while i <= q and j <= r: # p보다 q가 크고, q+1보다 r이 더 크면 반복
        if A[i] <= A[j]: #왼쪽의 첫번째 값보다 오른쪽의 첫번째 값이 더 크면
            tmp.append(A[i]) #왼쪽의 첫번째 값을 추가
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:   # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])
        i += 1

    while j <= r:   # 오른쪽 배열 부분이 남은 경우
        tmp.append(A[j])
        j += 1

    for t in range(len(tmp)): # 복사
         A[p + t] = tmp[t]

# 사용 예시:
A = [38, 27, 43 ,3 ,9 ,82 ,10]
merge_sort(A ,0,len( A)-1)
print( A )
