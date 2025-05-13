T = int(input())

for test_case in range(1, T+1):
    N, N_str= map(str, input().split())
    N = int(N)
    result = ''
    for ch in N_str:
        dec = int(ch, 16)
        bin_str = format(dec, '04b')
        result += bin_str

    print(f"#{test_case} {result}")