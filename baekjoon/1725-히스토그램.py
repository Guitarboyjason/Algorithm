# 크기는 해당 수보다 작은 수가 언제 나오느냐로 결정된다.
# 끝에 도달하였음에도 stack에 남아 있다면 마지막까지의 길이 * 높이
# 문제는 시작 지점보다 낮은 높이의 길다란 직사각형
# 결국 모든 높이에 대해 연속되는
# 작은 수가 나와서 pop을 해 줄 때 pop 되는 갯수를 cnt해서 갖고있으면 되려나
import sys
input = sys.stdin.readline
N = int(input())
histogram = [int(input()) for _ in range(N)] + [0]
max_size = 0
c = 0
size = []
# histogram.append(0)
stack = []

for i in range(N):
    cnt = 1
    while stack and histogram[stack[-1][0]] > histogram[i]:
        start, n_cnt = stack.pop()
        if max_size < histogram[start] * (i-start):
            max_size = histogram[start] * (i-start)
        cnt += n_cnt
        size.append(histogram[start] * (cnt))

    stack.append([i, cnt])
    print(stack)
    print(size)
# print(min(stack, key=lambda x: histogram[x[0]]))
cnt = 0
while stack:
    start, n_cnt = stack.pop()
    cnt += n_cnt
    if max_size < histogram[start] * (i-start):
        max_size = histogram[start] * (i-start)

    size.append(histogram[start] * (cnt))
print(stack)
print(size)
print(max_size)
print(max_size)
