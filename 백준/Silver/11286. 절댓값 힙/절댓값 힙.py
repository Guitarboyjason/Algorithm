import heapq,sys
input = sys.stdin.readline

arr = list()
N = int(input())
for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(arr,(abs(num),num))
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
