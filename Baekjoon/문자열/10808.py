def main():
    S = input().strip()
    counts = [0] * 26

    for ch in S:
        counts[ord(ch) - ord('a')] += 1

    print(*counts)

if __name__ == "__main__":
    main()
