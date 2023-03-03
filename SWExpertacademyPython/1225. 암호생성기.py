import sys
from collections import deque
sys.stdin = open("sources/input-10.txt", "r")


while True:
    try:
        test_case = int(input())
        arr = deque(map(int, input().split()))
        while 0 not in arr:
            for i in range(1, 6):
                next = arr.popleft()-i
                if next <= 0:
                    arr.append(0)
                    break
                else:
                    arr.append(next)
        print("#{}".format(test_case), end=" ")
        for i in arr:
            print("{}".format(i), end=" ")
        print()
    except:
        break
