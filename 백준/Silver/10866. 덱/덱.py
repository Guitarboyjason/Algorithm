command_list = ["push_front","push_back","pop_front","pop_back",\
                "size","empty","front","back"]
N = int(input())
commands = [input()for _ in range(N)]
deque = list()
for i in commands:
    if len(i) > 9:
        if command_list[0] in i:
            deque.insert(0,int(i[11:]))
        else:
            deque.append(int(i[10:]))
    else:
        command_index = command_list.index(i)
        if command_index == 2:
            if len(deque) > 0:
                print(deque.pop(0))
            else:
                print(-1)
        if command_index == 3:
            if len(deque) > 0:
                print(deque.pop())
            else:
                print(-1)
        if command_index == 4:
            print(len(deque))
        if command_index == 5:
            if len(deque) == 0:
                print(1)
            else:
                print(0)
        if command_index == 6:
            if len(deque) != 0:
                print(deque[0])
            else:
                print(-1)
        if command_index == 7:
            if len(deque) != 0:
                print(deque[-1])
            else:
                print(-1)

