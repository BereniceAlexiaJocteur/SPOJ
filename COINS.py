memo = {0: 0}


def rec(n):
    if n not in memo:
        memo[n] = max(n, sum([rec(n//i) for i in range(2, 5)]))
    return memo[n]


for i in range(10):
    n = int(input())
    print(rec(n))
