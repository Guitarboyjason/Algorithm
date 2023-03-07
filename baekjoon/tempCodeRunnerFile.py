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
        middle = (middle + start) // 2

    else:
        start = middle + 1
        middle = (end+middle)//2
print(middle)