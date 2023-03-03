
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    triangle = [[]for _ in range(N)]
    # print(triangle)
    # print(triangle[2])
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i-1][j] + triangle[i-1][j-1])
    print("#{}".format(test_case))
    for i in triangle:
        for j in i:
            print(j, end=" ")
        print()
