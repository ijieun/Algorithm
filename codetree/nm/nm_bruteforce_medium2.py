a = input()

# Write your code here!
# 이진수 찾는법: 2로 계속 나누고 나머지를 li 에 저장하고 반대로 출력 

def find_binary(a):
    # 이진수 길이가 11될때까지 반복 
    N = 0
    i = 1 
    while True:
        # 십진수 i를 이진수 구하는 반복 
        binary_i_li= []
        temp = i
        while True:
            if temp< 2:
                binary_i_li.append(temp)
                break
            binary_i_li.append(temp%2)
            temp //= 2
        binary_i_li = binary_i_li[::-1]

        if len(binary_i_li)>10:
            break 
        
        # 이진수가 한자리만 다른지 확인 
        count =0
        li_a = list(a)
        if len(binary_i_li) == len(li_a): 
            for j in range(len(binary_i_li)):
                if binary_i_li[j] != int(li_a[j]):
                    count += 1
                if count > 1:
                    break
        if count == 1:
            N = i
        # i는 십진수 
        
        i += 1
    return N
print(find_binary(a))


