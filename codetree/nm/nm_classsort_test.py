n = int(input())
# 4
# 1 5
# 1 7
# 3 6
# 1 10
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]
# [(1, 5, 1), (1, 7, 2), (3, 6, 3), (1, 10, 4)]
# Write your code here!

# 정렬. 키 작은 학생. 몸무게 더 큰 학생. 더 앞에.
# 번호는 순서대로 
print(students)

students.sort(key= lambda x: (x[0], -x[1]))
for student in students:
    print(student[0], student[1], student[2])