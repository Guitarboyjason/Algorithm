N,M = map(int,input().split())

arr = list(map(int,input().split()))

cnt = 0
index_start = 0
index_end = 0

summary = 0
while index_end!= N:
    summary += arr[index_end]
    if summary > M:
        while summary > M:      # 근본적으로 index_start는 index_end를 넘을 수 없다.
            summary -= arr[index_start]
            index_start += 1
    if summary == M:
        cnt += 1
    index_end += 1
print(cnt)
