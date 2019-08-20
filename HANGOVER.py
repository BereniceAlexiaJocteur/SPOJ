l = [0, 0]
count = 0
for i in range(2, 300):
    count += 1/i
    l.append(count)
while True:
    s = input()
    if s == "0.00":
        break
    x = float(s)
    print(str(l.index(min(filter(lambda j: j > x, l)))-1)+" card(s)")
