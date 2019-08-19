import math

n = int(input())
bound = int(math.log2(n))
l = [2**i for i in range(bound-1, bound+1)]
if n in l:
    print("TAK")
else:
    print("NIE")