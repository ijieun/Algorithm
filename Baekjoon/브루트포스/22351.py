s = input()
split_s = [i for i in s]
start = []
end = []
# 시작, 끝 생성
for i in range(1,4):
    start.append(int(''.join(split_s[:i])))
for j in range(1,4):
    end.append(int(''.join(split_s[len(split_s)-j:])))

result=[]
# 스트링 생성
for n in start:
    for m in end:
        if n>m:
            continue
        else:
            temp = ''.join([str(k) for k in range(n,m+1)])
            if s == temp:
                result.append([str(n),str(m)])
                break

print(' '.join(result[0]))