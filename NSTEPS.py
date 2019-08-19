nb_items = int(input())
for i in range(nb_items):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if x == y:
        n = x//2
        if 2*n == x:
            print(2*x)
        else:
            print(2*x-1)
    elif x-y == 2:
        n = y//2
        if 2*n == y:
            print(x+y)
        else:
            print(x+y-1)
    else:
        print("No Number")
