import sys, heapq
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    heapq.heappush(arr,int(input()))
for _ in range(len(arr)):
    print(heapq.heappop(arr))
