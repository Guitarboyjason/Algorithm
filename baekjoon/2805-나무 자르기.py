N,M = map(int,input().split())
trees = list(map(int,input().split()))
cut_height = max(trees) // 2
done_flag = False

while not done_flag:
    summary = 0
    for i in trees:
        if i - cut_height > 0:
            summary += i-cut_height
    if summary == M:
        done_flag = True
        break
    if summary > M:
        