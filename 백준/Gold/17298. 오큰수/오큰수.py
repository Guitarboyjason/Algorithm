N = int(input())
A = list(map(int, input().split()))

stack = []
NGE = [-1 for _ in range(N)]
stack.append(0)
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
print(*NGE)
