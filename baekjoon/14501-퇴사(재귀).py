def find_max(current,summary):
    if current == N+1 :
        return summary
    if arr[current][0] + current == N+1:        # N이 7일 경우
                                                # 8까지 확인 해야 하는데
                                                # 첫번째 배열의 합이 N+1을 넘어가버리는 경우
        return max(summary + arr[current][1],
                   find_max(current+1,summary))


    elif arr[current][0] + current > N+1 :
        return find_max(current+1,summary)
    else:
        return max(find_max(current+1,summary),
            find_max(arr[current][0] + current, summary + arr[current][1]))

N = int(input())

arr = [[-1]]

max_cost = [-1]*(N+1)
for _ in range(N):
    T, P = map(int,input().split())
    arr.append([T,P])
print(find_max(1,0))
