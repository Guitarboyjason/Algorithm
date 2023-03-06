# # N,M = map(int,input().split())
# # trees = list(map(int,input().split()))
# # cut_height = max(trees) // 2
# # done_flag = False

# # while not done_flag:
# #     summary = 0
# #     for i in trees:
# #         if i - cut_height > 0:
# #             summary += i-cut_height
# #     if summary == M:
# #         done_flag = True
# #         break
# #     if summary > M:
        
# N,M = map(int,input().split())
# tree_height = list(map(int,input().split()))

# def cut_trees(trees,cutting_position,M):
#     summary = 0
#     for i in trees:
#         if i >= cutting_position:
#             summary += i - cutting_position
#     if summary == M:
#         return cutting_position
#     if summary > M:
#         return 


N, M = map(int,input().split())
trees_height = list(map(int,input().split()))
start = 0
end = max(trees_height)
middle = (start+end)//2
while start <= end :
    tmp = [i - middle for i in trees_height if i - middle >= 0]
    if sum(tmp) == M:
        break
    elif sum(tmp) < M:
        M -= sum(tmp)
        trees_height = [i for i in trees_height if i - middle < 0] + [middle for _ in range(len(tmp))]
        end = middle - 1
        middle = (end + start) // 2

    else:
        start = middle + 1
        middle = (end+start)//2
print(middle)