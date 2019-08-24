while True:
    n = int(input())
    if n == 0:
        break
    cars = list(map(int, input().split(" ")))
    stack = []
    curr_number = 1
    test = True
    while len(cars) > 0:
        curr_car = cars[0]
        while len(stack) > 0 and stack[0] == curr_number:
            curr_number += 1
            del(stack[0])
        if curr_car == curr_number:
            curr_number += 1
            del(cars[0])
        else:
            stack.insert(0, curr_car)
            del(cars[0])
            if len(stack) > 1 and stack[0] > stack[1]:
                test = False
                break
    while len(stack) > 0 and stack[0] == curr_number:
        curr_number += 1
        del(stack[0])
    if test and stack == []:
        print("yes")
    else:
        print("no")