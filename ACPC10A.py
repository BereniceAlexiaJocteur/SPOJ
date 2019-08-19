while 1:
    x, y, z = input().split(" ")
    x = int(x)
    y = int(y)
    z = int(z)
    if x == y and x == 0:
        break
    med = (x+z)/2
    if y == med:
        print("AP "+str(2*z-y))
    else:
        print("GP "+str(int(z**2/y)))
