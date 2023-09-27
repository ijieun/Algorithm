g = input()
li = []
for i in g:
    if i=='(':
        li.append(i)
        a = li.index(i)

    elif i==')':
        if li:
            li.append(i)
            b = li.index(i)
            print(b-a)
            li.pop()
            li.pop()

print(li)