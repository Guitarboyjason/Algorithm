L_S = int(input())

S = list(map(int,input().split()))
n = int(input())

S.sort()


if n < min(S):
    print((n-1)*(min(S)-1-n+1) + min(S) - n - 1)
# 1 5 7
# 1 567
# 2 567
# 3 567
# 4 567
# 5 67
else:


    start_index = -1

    start = 0
    end = L_S-1
    k = -1
    while start<=end:
        mid = (start+end)//2
        if S[mid] == n:
            k = -1
            break
        elif S[mid] < n:
            k = mid
            start = mid+1
        else:
            end = mid-1

    start_index = k

    end_index = -1
    start = 0
    end = L_S-1
    k = -1
    while start<=end:
        mid = (start+end)//2
        if S[mid] == n:
            k = -1
            break
        elif S[mid] > n:
            k = mid
            end = mid-1
        else:
            start = mid+1

    end_index = k
    # 9 10 12
    # 7 10 12
    ## 10 11 12
    ## 7 8 9
    ## 7 101112
    ## 8 101112
    ## 9 101112
    ## 10 1112
    ## 2 * 2
    ## 1 * 3


    if start_index != -1 and end_index != -1:
        start_num = S[start_index] + 1
        end_num = S[end_index] - 1
        lft_cnt = n - start_num + 1
        rgt_cnt = end_num - n + 1
        print((lft_cnt-1)*rgt_cnt + (rgt_cnt-1))
    else:
        print(0)

    # 2 2 6
    # 1 * 4

    # 9 10 12
    ## 1 * 3
    ## 1 * 2


    # 34 ~ 59 ~ 99

