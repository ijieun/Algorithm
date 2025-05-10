import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = float(input().strip())
    bits = []
    frac = N
    overflow = False

    for _ in range(12):
        frac *= 2
        if frac >= 1.0:
            bits.append('1')
            frac -= 1.0
        else:
            bits.append('0')
        # 남은 분수가 0 이면 더 이상 계산할 필요 없음
        if abs(frac) < 1e-15:
            break

    # 12번 반복 후에도 frac != 0 이면 13자리 이상 필요
    if abs(frac) >= 1e-15:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc} {''.join(bits)}")
