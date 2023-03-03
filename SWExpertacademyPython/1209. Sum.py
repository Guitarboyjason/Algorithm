import sys
sys.stdin = open("sources/input-7.txt", "r")

for _ in range(1, 11):
    test_case = int(input())
    arr = []
    sum_list = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    for i in arr:
        sum_list.append(sum(i))
    for i in range(100):
        tmp = []
        for j in range(100):
            tmp.append(arr[j][i])
        sum_list.append(sum(tmp))
    tmp = []
    for i in range(100):
        tmp.append(arr[i][i])
    sum_list.append(sum(tmp))
    print("#{} {}".format(test_case, max(sum_list)))
