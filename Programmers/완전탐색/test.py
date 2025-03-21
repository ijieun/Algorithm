v = [[4,2], [4,3], [2,2]]
# ans = ?

x_dict = {}
y_dict = {}

# 사전 생성 
for i in range(3):
    x_dict[v[i][0]] = 0
    y_dict[v[i][1]] = 0

# 있으면 1씩 추가 
for i in range(3):
    x_dict[v[i][0]] += 1
    y_dict[v[i][1]] += 1

# x 딕셔너리의 key
for key in x_dict:
    if x_dict[key] ==1:
        x = key

# y 딕셔너리의 key
for key in y_dict:
    if y_dict[key] ==1:
        y = key

# 결과 출력 
print([x,y])