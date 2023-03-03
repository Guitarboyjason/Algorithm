N,M = map(int,input().split())
arr_pay_list  =[]
for _ in range(N):
    arr_pay_list.append(int(input()))

start = max(arr_pay_list)
end = sum(arr_pay_list)

while start <= end:

    middle = (start + end) // 2
    tmp_middle = middle
    cnt = 1
    for i in arr_pay_list:
        if tmp_middle < i:
            cnt += 1
            tmp_middle = middle
        tmp_middle -= i
    if cnt > M:        # 이럼 찾는 범위는 더 작은 곳에 있다.
        start = middle + 1
    else:
        end = middle - 1
        k = middle

print(k)
