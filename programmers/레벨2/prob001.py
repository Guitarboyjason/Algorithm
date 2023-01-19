import sys
sys.setrecursionlimit(10**6)

arr = [-1] * 100001
arr[0] = 0
arr[1] = 1
def fibonacci(n):
    if arr[n] != -1:
        return arr[n]
    arr[n] = fibonacci(n-1) + fibonacci(n-2)
    return arr[n]

print(fibonacci(3))
