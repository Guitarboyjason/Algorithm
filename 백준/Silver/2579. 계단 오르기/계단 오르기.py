# 마지막 계단을 무조건 밟아야 하므로,
# 1. 마지막 전 계단에서 올라온 경우.
# 2. 마지막 전전 계단에서 올라온 경우
# 로 나눌 수 있다.
# 그럼 마지막 전 계단까지의 최대의 숫자와,
# 마지막 전전 계단의 숫자까지의 최대 숫자를 비교하여 더 큰 수를 저장.

# 사실 이 조건만으로는 모든 계단을 밟고 올라오는 경우가 가장 크게 나올것.
# 세 계단 이상 연속으로 밟는 경우를 걸러내야 한다.
# 이차원 배열로 해서 두칸 건너 뛴 경우 [x, 0]으로 하고
# 한계단을 오를 경우 [x, +1]을 진행하여 [x, 2]가 되면 고려하지 않는 것으로
## DP가 아니라 재귀로는 풀 수 없나?


# def find_max_score(current):
#     # 예외처리 : 전전이 없는 경우, 전전전이 없는 경우
#     scores[]
#

stairs = int(input())
stairs_arr = [-1]
scores = [[-1,-1]]*(stairs+1)
# scores = [이전 계단(전전루트) , max(전전계단)]
for _ in range(stairs):
    stairs_arr.append(int(input()))

if stairs >= 1:
    scores[1] = [stairs_arr[1],-1]
if stairs >= 2:
    scores[2] = [scores[1][0]  + stairs_arr[2],stairs_arr[2]]
if stairs >= 3:
    # scores[3] = [scores[2][1], max(scores[1]) + stairs_arr[3]]
    for i in range(3,stairs+1):
        scores[i] = [scores[i-1][1]+stairs_arr[i], max(scores[i-2]) + stairs_arr[i]]
print(max(scores[stairs]))
