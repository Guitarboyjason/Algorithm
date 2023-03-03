K, N = map(int,input().split())
arr_Lan = []
for _ in range(K):
    arr_Lan.append(int(input()))

# N 이 K와 같은 경우 : arr에서 가장 작은 수를 출력하면 됨
# N 이 K보다 큰 경우 : 이게 문제긴 한데..
# 일단 큰걸 나눈다  ? ==> 3등분 하는경우는 어떡할거임
# 제일 작은 랜선의 길이를 기준으로 잡아야 할 듯,
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
