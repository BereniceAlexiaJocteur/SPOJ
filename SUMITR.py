for _ in range(int(input())):
    n = int(input())
    t = [list(map(int, input().split())) for _ in range(n)]
    for r in range(n-1, 0, -1):
        for c in range(0, r):
            t[r-1][c] += max(t[r][c], t[r][c+1])
    print(t[0][0])
