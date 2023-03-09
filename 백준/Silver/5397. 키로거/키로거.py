import sys
from collections import deque


# left  BAPC

# right
T = int(input())
for _ in range(T):
    keydown = input()

    left = []
    rev_right = []

    for i in keydown:
        if str(i) == str("<"):
            if len(left) > 0:
                rev_right.append(left.pop())
        elif i == '>':
            if len(rev_right) > 0:
                left.append(rev_right.pop())
        elif i == '-':
            if len(left) > 0:
                left.pop()
        else:
            left.append(i)
    print("".join(left + list(reversed(rev_right))))
