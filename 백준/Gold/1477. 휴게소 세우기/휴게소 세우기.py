# 휴게소 N개, 위치는 시작으로부터 얼마나 떨어져있는지
# M개를 더 세우려고 한다.
# 있는곳에 세울 수 없고, 끝에도 세울 수 없다.
# 정수 위치에만 세울 수 있다.

# 모든 휴게소 사이의 휴게소가 없는 구간의 길이의 최댓값을 최소

N,M,L = map(int,input().split())

shelter = list(map(int,input().split()))
shelter.extend([0,L])
shelter.sort()


start = 0
end = L
answer = 0
while start<end:
    mid = (start + end) // 2
    if mid == 0:
        break
    cnt = 0
    for i in range(1,len(shelter)):
        if shelter[i] - shelter[i-1] > mid:
            cnt += (shelter[i]-shelter[i-1]-1)//mid
    if cnt > M:
        start = mid + 1
    else:
        end = mid
        answer = mid
print(answer)