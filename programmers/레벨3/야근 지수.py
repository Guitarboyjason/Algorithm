#야근 피로도 = 야근 시작 시점에서의 **남은 일의 작업량
# N 시간동안 야근 피로도를 최소
# 1시간동안 작업량 1만큼 처리 가능
# 퇴근까지 남은 시간 N과 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값.

# def solution(n,works):
#     works.sort()
#     if len(works) == 1:
#         return (works[0]-n)**2
#     if sum(works) <= n:
#         return 0
#     diff = []
#     for i in range(len(works)-1):
#         diff.append(works[i+1]-works[i])
#     index = len(works)-2
#     while(n):
#         if diff[index] >= n:
#             for i in range(len(works)-1,index,-1):
#                 works[i] -= n//(len(works)-index)


import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    heap = []
    for i in works:
        heapq.heappush(heap,-i)
    while(n):
        tmp = -heapq.heappop(heap)
        tmp -=1
        n -= 1
        heapq.heappush(heap,-tmp)
    summary = 0
    for i in heap:
        summary += i**2
    return summary

print(solution(3,[1,1]))
