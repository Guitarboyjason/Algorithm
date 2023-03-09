N = int(input())
command = [input()for _ in range(N)]
stack = list()
for i in command:
    if i[0] == 'p' and len(i) > 3:
        stack.append(int(i[5:]))
    elif i[0] == 'p' and len(i) == 3:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    if i[0] == 's':
        print(len(stack))
    if i[0] == 'e':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if i[0] == 't':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
