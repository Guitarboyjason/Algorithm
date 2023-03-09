import heapq
import sys
input = sys.stdin.readline

max_heap = []       # 중요
min_heap = []
N = int(input())
for _ in range(N):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,-num)
    else:
        heapq.heappush(min_heap,num)
    if len(max_heap) >= 1 and len(min_heap) >= 1 and max_heap[0] * -1 > min_heap[0]:
        max_value = heapq.heappop(max_heap) * -1
        min_value = heapq.heappop(min_heap)

        heapq.heappush(max_heap,min_value*-1)
        heapq.heappush(min_heap,max_value)

    print(-max_heap[0])
