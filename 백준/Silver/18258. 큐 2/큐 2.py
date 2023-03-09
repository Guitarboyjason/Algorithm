from collections import deque


queue = deque()
result = []
for _ in range(int(input())):
    command = input()
    try:
        command_line, command_int = command.split()
        queue.append(command_int)
    except:
        if command == "front":
            if len(queue) == 0:
                result.append(-1)
            else:
                result.append(queue[0])
        if command == "pop":
            if len(queue) == 0:
                result.append(-1)
            else:
                result.append(queue.popleft())
        if command == "size":
            result.append(len(queue))
        if command == "empty":
            if len(queue):
                result.append(0)
            else:
                result.append(1)
        if command == "back":
            if len(queue):
                result.append(queue[-1])
            else:
                result.append(-1)
for i in result:
    print(i)
