new_list = []
sum=0
num = list(map(int, input().split())) 
for i in num:
    new_list.append(i*i)

for j in new_list:
    sum=sum+j

print(sum%10)
# solved!!
