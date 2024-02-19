# 최대 n/2마리. 
# 그냥 set으로 중복 제거해서 그걸 프린트 하면?
def solution(nums):
    answer = 0
    set_n = len(set(nums))
    if len(nums)//2 > set_n:
        print(set_n)
    else:
        print(round(len(nums)/2))
    return answer