N, K = map(int,input().split())
arr = [i for i in range(2,N+1)]

stack = list()
while arr:
    P = arr.pop(0)
    stack.append(P)
    finish = False
    cnt = 2
    while not finish:
        if len(arr) > 0 and P * cnt <= arr[-1]:
            if P*cnt in arr:
                stack.append(arr.pop(arr.index(P*cnt)))
        else:
            break
        cnt += 1
print(stack[K-1])


