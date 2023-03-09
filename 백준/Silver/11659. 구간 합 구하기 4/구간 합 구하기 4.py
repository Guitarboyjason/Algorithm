import sys
input= sys.stdin.readline
N,M = map(int,input().split())

num_list = [0] + list(map(int,input().split()))

accumulate_sum = [0]
for i in range(1,N+1):
    accumulate_sum.append(accumulate_sum[i-1]+num_list[i])

for _ in range(M):
    start_index,end_index = map(int,input().split())
    print(accumulate_sum[end_index]-accumulate_sum[start_index-1])