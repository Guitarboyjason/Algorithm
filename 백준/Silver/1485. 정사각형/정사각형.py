import math
T = int(input())
for test_case in range(T):
    x_list = []
    y_list = []
    for i in range(4):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    x, y = x_list[0], y_list[0]
    compare_list = set()

    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            compare_list.add(
                math.sqrt((x_list[i]-x_list[j])**2 + (y_list[i]-y_list[j])**2))
    if len(compare_list) != 2:
        print(0)
    if len(compare_list) == 2:
        print(1)
