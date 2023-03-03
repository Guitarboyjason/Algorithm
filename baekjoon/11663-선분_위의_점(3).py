import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dots = list(map(int,input().split()))
lines = []
for _ in range(M):
    lines.append(list(map(int,input().split())))


# 선분 시작점보다 크거나 같은,
# 선분 끝점보다 작거나 같은 점들을 찾아야 한다.
dots.sort()

def find_start_index(line):
    start = 0
    end = N-1
    k = -1
    while start<= end:
        middle = (start+end)//2
        if middle < 0 or middle > N-1:
            break
        if dots[middle] < line[0]:
            start = middle + 1
        else:
            end = middle - 1
            k = middle
    return k

def find_end_index(line):
    start = 0
    end = N-1
    k = -1
    while start<= end:
        middle = (start+end)//2
        if middle < 0 or middle > N-1:
            break
        if dots[middle] > line[1]:
            end = middle - 1
        else:
            start = middle + 1
            k = middle
    return k

for i in lines:
    if i[0] > dots[-1] or i[1] < dots[0]:
        print(0)
        continue
    start_index = find_start_index(i)
    end_index = find_end_index(i)
    print(end_index - start_index + 1)
