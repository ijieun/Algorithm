import sys
input = sys.stdin.readline
n, k = map(int, input().split())
li= list(map(int, input().split()))

def bubble_sort(a):
    count_ = 0
    result = -1
    for last in range(n, 0, -1):
        for i in range(0, last-1):
            if a[i]>a[i+1]:
                count_ += 1
                a[i], a[i+1] = a[i+1], a[i]
                if count_ == k:
                    result = f'{a[i]} {a[i+1]}'
    return result

print(bubble_sort(li))