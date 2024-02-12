"""
앞에서부터 확인해서 지뢰를 넣어본다?
아니면 주어진 지뢰 안에서 비교한다?

가장 앞과 가장 뒤는 0,1,2만 나올 수 있고
나머지는 3까지 가능
"""


# def updater(nums, graph, cnt):
#     bombs = [idx for idx, i in enumerate(graph) if i == "*"]
#     cnt += len(bombs)
#     for i in bombs:
#         nums[i] -= 1
#         if i - 1 >= 0:
#             nums[i - 1] -= 1
#         if i + 1 < N:
#             nums[i + 1] -= 1
#     graph = ["#" for _ in range(N)]
#     return nums, graph, cnt


for T in range(int(input())):
    N = int(input())
    nums = list(map(int, list(input())))
    graph = list(input())
    cnt = 0
    for idx in range(N):
        print(nums)
        if idx == 0:
            if nums[0] != 0 and nums[1] != 0:
                nums[0] -= 1
                nums[1] -= 1
                cnt += 1
        elif idx == N - 1:
            if nums[idx] != 0 and nums[idx - 1] != 0:
                nums[idx] -= 1
                nums[idx - 1] -= 1
                cnt += 1
        else:
            if (
                idx - 1 >= 0
                and idx + 1 < N
                and nums[idx - 1] != 0
                and nums[idx] != 0
                and nums[idx + 1] != 0
            ):
                nums[idx - 1] -= 1
                nums[idx] -= 1
                nums[idx + 1] -= 1
                cnt += 1
        # print(nums)
    print(cnt)
    #     i = nums[idx]
    #     if idx == 0:  # 처음
    #         if i != 0:
    #             if i == 2:
    #                 graph[0], graph[1] = "*", "*"
    #             else:
    #                 if N < 3 or graph[2] == 0:
    #                     graph[0] = "*"
    #     elif idx == N - 1:  # 마지막
    #         if i != 0:
    #             if i == 2:
    #                 graph[N - 1], graph[N - 2] = "*", "*"
    #             else:
    #                 if N < 3 or graph[N - 3] == 0:
    #                     graph[N - 1] = "*"

    #     else:  # 중간
    #         if i == 3:
    #             graph[idx - 1], graph[idx], graph[idx + 1] = "*", "*", "*"
    #         if i == 1:
    #             if idx - 1 >= 0 and graph[idx - 1] == 0 and idx + 1 < N:
    #                 graph[idx + 1] = "*"
    #             elif idx + 1 < N and graph[idx + 1] == 0 and idx - 1 >= 0:
    #                 graph[idx - 1] = "*"

    #     nums, graph, cnt = updater(nums, graph, cnt)
    #     print(nums)
    # print(cnt)
