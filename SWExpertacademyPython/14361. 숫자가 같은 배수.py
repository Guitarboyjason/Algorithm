# 1035 2070 3105

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    buff = []
    index = 0
    buff_count = [-1]*len(str(N))
    for i in str(N):
        if i not in buff:
            buff.append(i)
            buff_count[index] += 2
            index += 1
        else:
            buff_count[index] += 1
    arr = [2*N,3*N,4*N,5*N,6*N,7*N,8*N,9*N]
    sign = False
    for i in arr:
        if len(str(i)) == len(str(N)):
            tmp_count = buff_count.copy()       #갯수 비교군
            for j in str(i):
                if j in buff:                       #
                    if tmp_count[buff.index(j)] >= 1:
                        tmp_count[buff.index(j)] -= 1
                    else:   #tmp_count[buff.index(j)]가 0
                        break   #가능하지가 않다.
                else:       #buff에 j가 존재하지 않음
                    break
            sign = True

        if sign:
            break
    if not sign:
        print(f"#{test_case} impossible")
    else:
        print(f"#{test_case} possible")

