import sys
from collections import deque

def solve():
    t = int(input())
    for _ in range(t):
        n, m= map(int, input().split())
        priorities = list(map(int, input().split()))
        q = deque(enumerate(priorities))
        printed = 0 

        while q:
            idx, pri = q[0]
            if any(pri < other_pri for _, other_pri in q):
                q.rotate(-1)
            else:
                printed += 1 
                q.popleft()
                if idx ==m:
                    print(printed)
                    break 

if __name__ == "__main__":
    solve()