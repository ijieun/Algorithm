def solution(phone_book):
    # 접두사 비교
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 접두사 비교
        index = len(phone_book[i])
        if phone_book[i] in phone_book[i+1][:index]:
            return False
    return True
print(solution(["127", "1234", "12735", "567", "88"]))
