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
    mid = (start + end) // 2 # 찾고자 하는 최대 거리
    if mid == 0:
        break
    cnt = 0
    for i in range(1,len(shelter)):
        if shelter[i] - shelter[i-1] > mid:
            cnt += (shelter[i]-shelter[i-1]-1)//mid
            # 0 1000
            # mid = 500
            # 700 100 -> 600
            # 1
    if cnt > M:
        # 조건에 성립하지 않는다.
        # cnt가 너무 많다
        # ==세운 쉘터가 너무 많다
        # 우리가 찾고자하는 최대 거리 보다 mid가 작다
        # == mid가 더 커져야 cnt 값을 줄일 수 있다!
        start = mid + 1
    else:
        # 조건이 성립한다.
        # 성립은 하지만 최적의 값은 아닐 수도 있다.
        end = mid
        answer = mid
print(answer)