def solution(brown, yellow):
    answer = []
    edge = 4
    w_h_sum = (brown - edge) // 2
    yellow_divisors = [i for i in range(1, yellow+1) if yellow % i ==0]
    
    for d in yellow_divisors:
        p = yellow // d

        w, h = max(d, p), min(d,p)
        if w * h == yellow and w + h == w_h_sum:
            answer.append(w+2)
            answer.append(h+2)
            break
    return answer
print(solution(10,2))