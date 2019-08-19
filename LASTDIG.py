n = int(input())
for i in range(n):
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    print(pow(x, y, 10))
