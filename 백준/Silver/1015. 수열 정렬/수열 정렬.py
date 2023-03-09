def find_min(A_list):
    min_value = min(A_list)
    min_index = A_list.index(min(A_list))
    return min_index




N = int(input())
A_list = [int(x) for x in input().split()]
B_list = [-1 for _ in range(N)]

for i in range(N):
    min_index = find_min(A_list)
    B_list[min_index] = i
    A_list[min_index] = 1001

for i in B_list:
    print(i,end=" ")