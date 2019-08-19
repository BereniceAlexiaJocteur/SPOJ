nb_items = int(input())
for i in range(nb_items):
    s = input()
    print(s[:len(s) // 2:2])
