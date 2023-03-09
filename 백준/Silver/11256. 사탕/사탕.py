T = int(input())

for _ in range(T):
    J,N = map(int,input().split())
    arr_N = []
    for i in range(N):
        R,C = map(int,input().split())
        arr_N.append(R*C)
    arr_N.sort(reverse=True)
    count = 0
    for i in arr_N:
        if J > 0:
            count += 1
            J -= i
    print(count)

