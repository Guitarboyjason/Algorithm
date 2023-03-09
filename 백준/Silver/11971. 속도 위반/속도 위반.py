# N개의 구간으로 나뉘고, 길이, 제한속도가 주어진다.
# 도로 길이의 총 합은 100

# 연정이가 달린 도로도 따로 나뉜다. 속도도.

N,M = map(int,input().split())
arr_N = [list(map(int,input().split()))for _ in range(N)]
arr_M = [list(map(int,input().split()))for _ in range(M)]

max_illegal = 0
for i in range(100):
    tmp = i
    index = 0
    # for j in range(len(arr_N)):
    #     if tmp > arr_N[j][0]:
    #         tmp -= arr_N[j][0]
    #         index = j
    #     else:
    #         break
    while tmp > 0:
        tmp -= arr_N[index][0]
        index += 1
    limit = arr_N[index-1][1]

    tmp = i
    index = 0
    # for j in range(len(arr_M)):
    #     if tmp > arr_M[j][0]:
    #         tmp -= arr_M[j][0]
    #         index = j
    #     else:
    #         break
    while tmp > 0:
        tmp -= arr_M[index][0]
        index += 1
    speed = arr_M[index-1][1]

    if max_illegal < speed - limit:
        max_illegal = speed - limit
print(max_illegal)
