# M개의 블루레이는 모두 같은 크기, 블루레이의 크기를 최소로.
# 강의의 길이가 분 단위로 주어진다. 가능한 블루레이의 크기 중 최소

# (N <= 100,000) (M <= N)

N,M = map(int,input().split())
lesson_time = list(map(int,input().split()))

# M 개로 나눈다고 할 때, 영상의 최대 길이는 sum(lesson_time). min =0
#

start = max(lesson_time)       # 이게 최적의 수긴 하다.
end = sum(lesson_time)
# 어떻게 구분지어서 넣을지가 중요하겠다.
# 저 start 부터 확인을 한다면 결국 최선으로 더하는 수가 ? 되면 ? 인가 ?


while start <= end:
    mid = (start+end) // 2
    cnt = 1
    summary = 0
    for i in lesson_time:
        if summary + i <= mid:
            summary += i
        else:
            cnt += 1
            summary = i
    if cnt > M:     # cnt의 수가 많아졌다는 뜻은 충분히 크게 자르지 않았다는 것
        start = mid + 1
    else:
        k = mid
        end = mid - 1
print(k)

