n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!

min_width = 99999

for i in range(n):
    x_li = []
    y_li = []
    for j in range(n):
       
        if i==j:
            continue
        x_li.append(x[j])
        y_li.append(y[j])

    min_x = min(x_li)
    min_y = min(y_li)

    max_x = max(x_li)
    max_y = max(y_li)

    width = abs(max_x- min_x) * abs(max_y - min_y)
    min_width = min(min_width, width)

print(min_width)

