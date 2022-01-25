n = int(input())
stack = []
most = []

for i in range(n):
    inp = input().split(' ')
    x = int(inp[0])
    d = 0
    if len(inp) > 1: d = int(inp[1])
    if x == 1:
        stack.append(d)
        if not most or most[-1] <= d: most.append(d)
    elif x == 2:
        d = stack.pop()
        if most[-1] == d: most.pop()
    else:
        print(most[-1])
