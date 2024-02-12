# 크기는 해당 수보다 작은 수가 언제 나오느냐로 결정된다.
# 끝에 도달하였음에도 stack에 남아 있다면 마지막까지의 길이 * 높이
# 문제는 시작 지점보다 낮은 높이의 길다란 직사각형
# 작은 수가 나와서 pop을 해 줄 때 길이를 알 수 있으면 될 것 같다.
import sys

input = sys.stdin.readline
N = int(input())
histogram = [int(input()) for _ in range(N)] + [0]
max_size = 0
c = 0
stack = []

for i in range(N + 1):
    c = i
    while stack and stack[-1][0] > histogram[i]:
        h, old_c = stack.pop()
        if h * (i - old_c) > max_size:
            max_size = h * (i - old_c)
        c = old_c

    stack.append([histogram[i], c])

print(max_size)
