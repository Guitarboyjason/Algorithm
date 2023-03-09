K, N = map(int,input().split())
arr_Lan = []
for _ in range(K):
    arr_Lan.append(int(input()))

    
start = 1
end = max(arr_Lan)
while(start<=end):
    mid = (start+end)//2
    cnt = 0
    for i in arr_Lan:
        cnt += i // mid
    if cnt >= N:        #할 수 있는 최선을 구함
        start = mid+1
    else:
        end = mid-1
print(end)
