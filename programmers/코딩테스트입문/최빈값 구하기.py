def solution(array):
    max_count = 0
    max_index = 0
    arr = [array.count(i) for i in array]
    arr = list(set(zip(arr,array)))
    sign = 0
    max_count,max_num = max(arr,key=lambda x : x[0])
    for i in arr:
        if max_count == i[0]:
            if sign == 0:
                sign = 1
            else:
                sign = 0
                break

    if sign:
        print(max_num)
    else:
        print(-1)

    answer = 0
    return answer

solution([1])
