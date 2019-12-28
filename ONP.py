def convert(string):
    number = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w",
              "x", "c", "v", "b", "n"]
    operator = {"+": 1, "-": 2, "*": 3, "/": 4, "^": 5}
    queue = []
    stack = []
    for i in string:
        if i in number:
            queue.append(i)
        elif i in operator:
            while stack[-1] in operator and operator[stack[-1]] > operator[i]:
                queue.append(stack.pop())
            stack.append(i)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()
    while stack:
        queue.append(stack.pop())
    return ''.join(queue)


n = int(input())
for j in range(n):
    print(convert(input()))
