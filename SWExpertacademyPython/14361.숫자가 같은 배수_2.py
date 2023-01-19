T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    compare_arr = []
    seperated_N = list(set(i for i in str(N)))
    for i in range(2,10):       #자리 수 확인하면서 비교군에 저장
        if len(str(N)) == len(str(N*i)):
            compare_arr.append(N*i)
        else:
            break
    compare_count = [str(N).count(i) for i in seperated_N]
    # print(compare_arr)
    # print(seperated_N)
    # print(compare_count)
    can_sign = False
    printed_sign = False
    for i in compare_arr:   #여기서부터 가능한지 확인해보는 과정
        tmp_compare_count = compare_count.copy()
        for j in str(i):
            can_sign = True
            if j in seperated_N:
                if tmp_compare_count[seperated_N.index(j)] >= 1:
                    tmp_compare_count[seperated_N.index(j)] -= 1
                else:
                    can_sign = False
                    break
            else:
                can_sign = False
                break
        if can_sign:
            print(f"#{test_case} possible")
            printed_sign = True
            break
    if not printed_sign:
        print(f"#{test_case} impossible")





