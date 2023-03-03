import sys
sys.stdin = open("sources/input-9.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    arr = input()
    pattern = []
    sign = 0
    for i in range(len(arr)):
        if arr[i] in pattern:
            sign = 1
            for j in range(len(pattern)):
                # print(arr[i+j], pattern[j])
                if arr[i+j] != pattern[j]:
                    sign = 0
            if sign:
                print("#{} {}".format(test_case, len(pattern)))
                break
        # print(pattern)
        pattern.append(arr[i])
