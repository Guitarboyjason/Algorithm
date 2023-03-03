# import sys
# import numpy as np
# sys.stdin = open("sources/input-5.txt", "r")


# def count_flies():
#     global tmp
#     global N, M
#     flies = []
#     for i in range(N-M+1):  # 0123
#         for j in range(N-M+1):  # 0123
#             # print(arr[i:i+M][j:j+M])
#             # summary += arr[i][j]
#             flies.append(sum(sum(tmp[i:i+M, j:j+M])))  # [0:2,0:2] [2:4, ]
#     return max(flies)


# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = []
#     for i in range(N):
#         arr.append(list(map(int, input().split())))
#     tmp = np.array(arr)
#     print("#{} {}".format(test_case, count_flies()))


# numpy가 안되네

import sys
sys.stdin = open("sources/input-5.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    max_flies = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            flies = []
            for k in range(M):
                for l in range(M):
                    flies.append(arr[i+k][j+l])
            max_flies.append(sum(flies))
    print("#{} {}".format(test_case, max(max_flies)))
