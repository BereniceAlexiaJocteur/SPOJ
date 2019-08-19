import math

n = int(input())
root = int(math.sqrt(n))
s = root - (root*(root+1)) // 2
for i in range(1, root+1):
    s += n//i
print(s)
