t = int(input())
for j in range(t):
    n = int(input())
    l = dict()
    for i in range(n):
        account = input()
        if account not in l:
            l[account] = 1
        else:
            l[account] += 1
    for k in sorted(l):
        print(str(k)+" "+str(l[k]))
    garbage = input()
    if j < (t-1):
        print("\n")
