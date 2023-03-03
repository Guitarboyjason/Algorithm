# N,M = map(int,input().split())
# trees = list(map(int,input().split()))
# cut_height = max(trees) // 2
# done_flag = False

# while not done_flag:
#     summary = 0
#     for i in trees:
#         if i - cut_height > 0:
#             summary += i-cut_height
#     if summary == M:
#         done_flag = True
#         break
#     if summary > M:
        
N,M = map(int,input().split())
tree_height = list(map(int,input().split()))

def cut_trees(trees,cutting_position,M):
    summary = 0
    for i in trees:
        if i >= cutting_position:
            summary += i - cutting_position
    if summary == M:
        return cutting_position
    if summary > M:
        return 
