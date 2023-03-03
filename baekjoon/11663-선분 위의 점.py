N,M = map(int,input().split())
dots = list(map(int,input().split()))
lines = []
for _ in range(M):
    lines.append(list(map(int,input().split())))

dots.sort()
# 점의 갯수와 선분의 갯수가 많이 때문에,
# 이분 탐색으로 시작점과 같거나 크고, 끝점보다 작거나 같은 점들을 확인한다.


for i in lines:
    i.sort()
    start = 0
    end = len(dots)-1
    k = start
    start_index = start
    end_index = end
    while start <= end:
        if dots[start] > i[0]:
            start_index = k
            break
        elif dots[start] == i[0]:
            start_index = start
            break
        middle = (start+end) //2
        if dots[middle] <= i[0]:
            start = middle+1
            k = start
        else:
            end = middle-1
    start = 0
    end = len(dots)-1
    k = end
    while start <= end:
        if dots[end] < i[1]:
            end_index = k
            break
        elif dots[end] == i[1]:
            end_index = end
            break
        middle = (start+end) //2
        if dots[middle] <= i[0]:
            start = middle+1
        else:
            k = end
            end = middle-1
    print(end_index-start_index + 1)
