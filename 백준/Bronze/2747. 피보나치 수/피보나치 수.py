n = int(input())
arr_fibonacci = [-1 for _ in range(n+1)]
arr_fibonacci[0] = 0
arr_fibonacci[1] = 1
def find_fibonacci(n):
    if arr_fibonacci[n] != -1:
        return arr_fibonacci[n]
    else:
        arr_fibonacci[n] = find_fibonacci(n-1) + find_fibonacci(n-2)
        return arr_fibonacci[n]
print(find_fibonacci(n))


