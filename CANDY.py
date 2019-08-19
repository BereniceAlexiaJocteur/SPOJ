while True:
    n = int(input())
    if n == -1:
        break
    l = []
    for i in range(n):
        l.append(int(input()))
    s = sum(l)
    if s % n != 0:
        print(-1)
    else:
        count = 0
        m = s//n
        for i in l:
            count += max(0, m-i)
        print(count)
