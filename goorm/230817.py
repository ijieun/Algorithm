n = int(input())
k = list(map(int,input().split()))
max_k = k.index(max(k))

f1=k[0:max_k]
f2=sorted(k[0:max_k])
b1=k[max_k:n]
b2=list(reversed(sorted(k[max_k:n])))

if(f1==f2) and (b1==b2):
	print(sum(k))
else:
	print(0)
