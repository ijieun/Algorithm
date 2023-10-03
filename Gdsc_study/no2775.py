# 첫 입력만큼 반복
for i in range(int(input())):
    def S(k, n):
        if k == 0:
            # n을 바로 리턴
            return n
        else:
            sum = 0
            for i in range(1,n+1):
                sum += S(k-1,i)
                # 한층 밑의 1호~i호의 합 리턴
            return sum 
# k는 층, n은 호
    k = int(input())
    n = int(input())
    print(S(k,n))