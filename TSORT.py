nb_items = int(input())
l = []
for i in range(nb_items):
    n = int(input())
    l.append(n)
l.sort()
for i in l:
    print(i)
