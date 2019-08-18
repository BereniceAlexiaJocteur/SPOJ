nb_items = int(input())

for i in range(nb_items):
    m, n = input().split(" ")
    m = int(str(m)[::-1])
    n = int(str(n)[::-1])
    som = int(str(m+n)[::-1])
    print(som)
