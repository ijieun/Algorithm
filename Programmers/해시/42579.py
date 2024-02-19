# defaultdict, enumerate, zip 이용
from collections import defaultdict

def solution(genres, plays):
    answer = []

    genres_order = defaultdict(int)
    genres_plays = defaultdict(list)
    
    # 장르, 재생시간을 zip해서 index 붙임
    for i, (genre, v) in enumerate(zip(genres, plays)):
        # 합계를 구함
        genres_order[genre] += v
        # 장르빼고 인덱스, 재생시간을 append
        genres_plays[genre].append((i,v))

    # 내림차순 정렬
    for genre, _ in sorted(genres_order.items(), key=lambda x:-x[1]):
        # 내림차순 정렬해서 2개만 출력
        for i, v in sorted(genres_plays[genre], key=lambda x:-x[1])[:2]:
            answer.append(i)
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))