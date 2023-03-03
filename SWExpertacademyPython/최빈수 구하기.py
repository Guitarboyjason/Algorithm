# f = open("sources/input.txt", "r")
# T = int(f.readline())
T = int(input())
for _ in range(T):
    # testcase = int(f.readline())
    testcase = int(input())
    # arr = list(map(int, f.readline().split()))
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    arr2 = []
    for i in arr:
        arr2.append(arr.count(i))
    print(f"#{testcase} {arr[arr2.index(max(arr2))]}")

# for _ in range(T):
# test_case = int(input())
# arr = list(map(int, input().split()))
#  arr.sort(reverse=True)
#   arr_count = []
#    for j in arr:
#         arr_count.append(arr.count(j))
#     max_index = arr_count.index(max(arr_count))
#     print(f"#{test_case} {arr_count[max_index]}")
