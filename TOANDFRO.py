while True:
    n = int(input())
    if n == 0:
        break
    s = input()
    res = []
    q, r = divmod(len(s), 2*n)
    for i in range(q):
        res.append(list(s[2*i*n:(2*i+1)*n]))
        res.append(list(reversed(s[(2*i+1)*n:2*(i+1)*n])))
    if r:
        res.append(list(s[-n:]))
    res_string = ""
    for i in range(n):
        for j in range(len(res)):
            res_string += res[j][i]
    print(res_string)
