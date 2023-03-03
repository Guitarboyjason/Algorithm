
import sys
sys.stdin = open("sources/input-12.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    arr = []
    for _ in range(8):
        arr.append(input())
    cnt = 0

    for i in range(8-n+1):
        for j in range(8-n+1):
            if i == 0 and j == 4:
                pass
            middle = j + n//2
            sign_x = 1
            sign_y = 1
            for k in range(n//2):
                if n % 2 == 1:
                    if arr[i][middle-k] != arr[i][middle+k]:
                        sign_x = 0
                    if arr[middle-k][i] == arr[middle+k][i]:
                        sign_y = 0
                else:
                    if arr[i][middle-k-1] != arr[i][middle+k]:
                        sign_x = 0
                    if arr[middle-k-1][i] == arr[middle+k][i]:
                        sign_y = 0

            if sign_x:
                cnt += 1
            if sign_y:
                cnt += 1
    print("#{} {}".format(test_case, cnt))
