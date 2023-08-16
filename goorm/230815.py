n = int(input())
t,m = map(int, input().split())
for _ in range (n):
	c = int(input())
	m = m+c
if(m>59):
	t=t+m//60
	m=m%60
	if(t>23):
		t=t%24
	print(t,m)
else:
	print(t,m)
