# 생성자
# sum(map(int, str())) 으로 숫자 출력할 수 있음.
li = []
for i in range(1,10001):
    li.append(i+sum(map(int, str(i))))
for i in range(1,10001):
    if i not in li:
        print(i)