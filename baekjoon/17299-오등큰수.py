N = int(input())
A = list(map(int, input().split()))

F = dict()

for i in A:
    if i not in F:
        F[i] = 1
    else:
        F[i] += 1
stack = []
stack.append(0)
NGF = [-1 for _ in range(N)]

for i in range(1, N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        NGF[stack.pop()] = A[i]
    stack.append(i)
print(*NGF)
