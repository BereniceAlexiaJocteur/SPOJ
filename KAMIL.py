l=["T","D","L","F"]
for i in range(10):
    s=input()
    print(2**sum([s.count(j)for j in l]))