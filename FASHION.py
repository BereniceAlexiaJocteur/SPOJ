for _ in range(int(input())):
    n = int(input())
    male = [int(i) for i in input().split(" ")]
    female = [int(i) for i in input().split(" ")]
    male.sort()
    female.sort()
    print(sum([x*y for x, y in zip(male, female)]))
