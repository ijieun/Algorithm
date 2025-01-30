import sys 
n = int(input())
arr = [int(input()) for _ in range(n)]
# [522, 6, 84, 7311, 19, 9999]

# Write your code here!
max_value = -99999
carry_happened = False 

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            value = []
            carry_happened = False
            for l in range(4):
                fir_li = list(str(arr[i]))[::-1]
                sec_li = list(str(arr[j]))[::-1]
                thr_li = list(str(arr[k]))[::-1]
                # 전부 4자리로 맞춰줌. 
                if len(fir_li)<4:
                    [fir_li.append('0') for _ in range(4-len(fir_li))]
                if len(sec_li)<4:
                    [sec_li.append('0') for _ in range(4-len(sec_li))]
                if len(thr_li)<4:
                    [thr_li.append('0') for _ in range(4-len(thr_li))]
                # 그대로면 캐리 아님. 값 계산. 
                if (int(fir_li[l])+int(sec_li[l])+int(thr_li[l]))%10==(int(fir_li[l])+int(sec_li[l])+int(thr_li[l])):
                    value.append(int(fir_li[l])+int(sec_li[l])+int(thr_li[l]))
                else:
                    carry_happened = True
                    break
            if carry_happened == True:
                continue
                    # print(int(fir_li[l])+int(sec_li[l])+int(thr_li[l]))
                    # print(f"({int(fir_li[l])}+{int(sec_li[l])}+{int(thr_li[l])})")
            value = value[::-1]
            str_value = "".join(map(str,value))
            # print(str_value, type(str_value))
            if str_value !='':
                str_value = int(str_value)
            else:
                str_value = 0
            max_value = max(max_value, str_value)

if carry_happened==True or max_value==-99999:
    print(-1)
else:
    print(max_value)
