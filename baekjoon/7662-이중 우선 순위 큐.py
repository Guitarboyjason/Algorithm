# # import sys
# # sys.stdin = open("baekjoon/input.txt","r")
# # input = sys.stdin.readline
# # import heapq
# # def I(num):
# #     global min_Q,max_Q
# #     heapq.heappush(min_Q,num)
# #     heapq.heappush(max_Q,-num)
    
# # def D(num):
# #     global min_Q,max_Q
# #     # if not Q:
# #     #     return
# #     if num == -1:
# #         if not min_Q:
# #         heapq.
# #             return
# #         tmp = heapq.heappop(min_Q)
# #         # max_Q.index(tmp)
# #         max_Q.remove(-tmp)
# #         heapq.heapify(max_Q)
# #     else:
# #         if not max_Q:
# #             return
# #         tmp = heapq.heappop(max_Q)
# #         min_Q.remove(-tmp)
# #         heapq.heapify(min_Q)
        
        
# # for T in range(int(input())):
# #     k = int(input())
# #     min_Q = []
# #     max_Q = []
# #     for _ in range(k):
# #         command,n = input().split()
# #         n = int(n)
# #         locals()[command](n)
# #     answer = []
# #     if not min_Q:
# #         answer.append("EMPTY")
# #     elif len(min_Q) == 1:
# #         tmp = heapq.heappop(min_Q)
# #         answer.append(tmp)
# #         answer.append(tmp)
# #     else:
# #         # answer.append(0)
# #         answer.append(-heapq.heappop(max_Q))
# #         # Q = [-i for i in Q]
# #         # heapq.heapify(Q)
# #         answer.append(heapq.heappop(min_Q))
# #     print(*answer)

# import heapq
# import sys
# sys.stdin = open("baekjoon/input.txt","r")
# input = sys.stdin.readline

# for T in range(int(input())):
#     Q = []
#     k = int(input())
#     for _ in range(k):
#         command,n = input().split()
#         n = int(n)
#         if command =="D":
#             if not Q:
#                 continue
#             if n == -1:
#                 heapq.heappop(Q)
#             else:
#                 Q = heapq.nlargest(len(Q),Q)[1:]
#                 heapq.heapify(Q)
#         else:
#             heapq.heappush(Q,n)
#     answer = []
#     if Q:
#         answer.append(heapq.nlargest(1,Q)[0])
#         answer.append(heapq.heappop(Q))
#     else:
#         answer.append("EMPTY")
#     print(*answer)


import heapq
import sys
sys.stdin = open("baekjoon/input.txt","r")
input = sys.stdin.readline

for T in range(int(input())):
    k = int(input())
    max_q = []
    hq = []
    visited = [False]*1_000_001
    for i in range(k):
        command = input().split()
        if command[0] == "I":
            heapq.heappush(hq,(int(command[1]),i))
            heapq.heappush(max_q,(-int(command[1]),i))
            visited[i] = True
        elif command[1] == "1":
            while max_q and not visited[max_q[0][1]]:
                heapq.heappop(max_q)
            if max_q:
                visited[heapq.heappop(max_q)[1]]=False
        else:
            while hq and not visited[hq[0][1]]:
                heapq.heappop(hq)
            if hq:
                visited[heapq.heappop(hq)[1]] = False
    answer = []
    while hq and not visited[hq[0][1]]:
        heapq.heappop(hq)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
    if max_q:
        answer.extend([-max_q[0][0],hq[0][0]])
    else:
        answer.append("EMPTY")
    print(*answer)