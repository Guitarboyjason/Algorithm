# # N개의 물건
# # Weight, Value
# # 최대 K만큼의 무게
# # 물건들의 가치의 최댓값은?
#
# # 모든 경우의 수는?
# # 물건의 수 100
# # 그럼 총 2**100의 경우의 수가 나온다.
# # 너무 많긴하네
#
# # 그리디 ?
# # 만약 앞으로 고려해야 할 물품들의 무게 합이 여유가 있을 때
# # 다 가져가는걸로 하자.
#
#
# N,K = map(int,input().split())
# things = [list(map(int,input().split()))for _ in range(N)]
#
# things.sort(key=lambda x:x[0])
# things.sort(key=lambda x:x[1],reverse=True)
#
# arr = [i for i in things if i[1] > 10]
#
# def max_value_recursive(things,K):
#     if K == 0:
#         return 0
#     can_list = list(i for i in things if i[0] <= K)
#     if len(can_list) >= 1:
#         return max((can_list[0][1] + max_value_recursive(can_list,K-can_list[0][0])),\
#                    max_value_recursive(can_list[1:],K))
#     else:
#         return 0
# print(max_value_recursive(things,K))

def knapsack(capacity,n):
    arr = [[0for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for s in range(1,capacity+1):
            if things[i-1][0] > s:
                arr[i][s] = arr[i-1][s]
            else:
                arr[i][s] = max(things[i-1][1] + arr[i-1][s-things[i-1][0]],\
                                arr[i-1][s])
    return arr[n][capacity]

N,K = map(int,input().split())
things = [list(map(int,input().split()))for _ in range(N)]
print(knapsack(K,N))
