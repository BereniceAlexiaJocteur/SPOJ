n = int(input())
for i in range(n):
    nbkids = input()
    nbkids = int(input())
    s = 0
    for i in range(nbkids):
        s = (s + int(input())) % nbkids
    if s == 0:
        print("YES")
    else:
        print("NO")
