list = []

for i in range(9):
    num = int(input())
    list.append(num)
print(max(list))
print(list.index(max(list))+1)