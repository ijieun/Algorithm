# 몸무게, 키 모두 자신보다 큰 사람의 개수 구하기
# 그 개수가 답.

li = []
cnt = 0
score = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    li.append([x,y])
    
for i in range(n):
    count = 1
    for j in range(n):
        # i보다 비교하는 j의 키, 몸무게가 더 크면 count 1증가
        if li[i][0]<li[j][0] and li[i][1]<li[j][1]:
            count += 1
    score.append(count)
print(score)