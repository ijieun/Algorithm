# 딕셔너리로 풀기
# 1. 입력받기
# 2. 해당 값에 있으면 위치에 +1씩 하기
# 3. max 값의 숫자를 출력

import sys
input = sys.stdin.readline

card_dict = {}
n = int(input())
for _ in range(n):
    card = int(input())
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] =1
print(sorted(card_dict.items(), key=lambda x:(-x[1], x[0]))[0][0])