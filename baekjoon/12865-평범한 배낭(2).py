def sol():
    N, K = map(int,input().split())
    arr_items = [[0,0]]
    for _ in range(N):
        arr_items.append(list(map(int,input().split())))

    max_value_arr = [0]*(K+1)      # 이 무게에서 가장 많이 들 수 있는 배열


    for i in range(1,N+1):  #모든 아이템을 확인함
        for w in range(1,K+1):  #무게별로 최댓값을 구함
            if arr_items[i][0]<= w :
                max_value_arr[w] = max(max_value_arr[w],arr_items[i][1]+max_value_arr[w-arr_items[i][0]])
    
    print(max(max_value_arr))

sol()
            