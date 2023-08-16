t = int(input())
l =[]
for _ in range(t):
	c = input().split()
	if(c[1]=='+'):
		l.append(int(c[0])+int(c[2]))
	if(c[1]=='-'):
		l.append(int(c[0])-int(c[2]))
	if(c[1]=='*'):
		l.append(int(c[0])*int(c[2]))
	if(c[1]=='/'):
		l.append(int(c[0])//int(c[2]))
print(sum(l))
