nb_items = int(input())
factorials = [0 for _ in range(101)]
factorials[0] = 1
curr_max_n = 0
for i in range(nb_items):
    n = int(input())
    if n > curr_max_n:
        for j in range(curr_max_n+1, n+1):
            factorials[j] = factorials[j-1]*j
        curr_max_n = n
    print(factorials[n])
