def get_num_5(n):
    s = 0
    p = 5
    t = n // p
    while t > 0:
        s += t
        p *= 5
        t = n // p
    return s


nb_items = int(input())
for i in range(nb_items):
    print(get_num_5(int(input())))
