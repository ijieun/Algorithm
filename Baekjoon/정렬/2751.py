def merge_sort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    # l이 low_arr의 길이보다 커지고, h가 high_arr의 길이보다 커지면 중지
    while l<len(low_arr) and h< len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l+=1
        else:
            merged_arr.append(high_arr[h])
            h+=1
    # 남은 값들은 그냥 몽땅 넣어줌.
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

list = []
n = int(input())
for _ in range(n):
    num = int(input())
    list.append(num)
for each in merge_sort(list):
    print(each)