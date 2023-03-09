N = int(input())

queue = list()
commands = [input()for _ in range(N)]
for i in commands:
    if i[0] == 'p' and len(i)>3:
        queue.append(int(i[5:]))
    elif i[0] == 'p' and len(i) == 3:
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
    if i[0] == 's':
        print(len(queue))
    if i[0] == 'e':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if i[0] == 'f':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    if i[0] == 'b':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
