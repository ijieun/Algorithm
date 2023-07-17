dish = list(input())
result = 0
for i in range(1,len(dish)):
    if(dish[i]==dish[i-1]):
        result+=5
            
    else:
        result+=10
print(result+10)
# solved!!!