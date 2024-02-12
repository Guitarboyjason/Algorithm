# def sol():
#     N, K = map(int,input().split())
#     arr_items = [[0,0]]
#     for _ in range(N):
#         arr_items.append(list(map(int,input().split())))

#     max_value_arr = [0]*(K+1)      # 이 무게에서 가장 많이 들 수 있는 배열


#     for i in range(1,N+1):  #모든 아이템을 확인함
#         for w in range(1,K+1):  #무게별로 최댓값을 구함
#             if arr_items[i][0]<= w :
#                 max_value_arr[w] = max(max_value_arr[w],arr_items[i][1]+max_value_arr[w-arr_items[i][0]])
    
#     print(max(max_value_arr))

# sol()

# N,K = map(int,input().split())
# things = [[0,0]]+[list(map(int,input().split())) for _ in range(N)]
# max_value_arr = [0] * (K+1)
# for i in range(1,N+1):      # 모든 물건을 조사
#     for w in range(1,K+1):  # 모든 무게에 대해 저장
#         if things[i][0] <= w:
#             max_value_arr[w] = max(max_value_arr[w],things[i][1]+max_value_arr[w-things[i][0]])

# # print(things)
# print(max(max_value_arr))

# N,K = map(int,input().split())
# things = [[0,0]]+[list(map(int,input().split()))for _ in range(N)]
# arr = [[0 for _ in range(K+1)] for _ in range(N+1)]
# for i in range(1,N+1):
#     for w in range(1,K+1):
#         if things[i][0] > w:
#             arr[i][w] = arr[i-1][w]
#         else:
#             arr[i][w] = max(things[i-1][1] + arr[i-1][w-things[i-1][0]], arr[i-1][w])
# print(arr[N][K])

def knapsack(capacity,n):
    arr = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for s in range(1,capacity+1):
            if things[i][0] > s:
                arr[i][s] = arr[i-1][s]
            else:
                arr[i][s] = max(things[i][1] + arr[i-1][s-things[i][0]],\
                                arr[i-1][s])#물건을 넣었을 때와 물건을 넣지 않았을 때
    return arr[n][capacity]

N,K = map(int,input().split())
things = [[0,0]]+[list(map(int,input().split()))for _ in range(N)]
print(knapsack(K,N))