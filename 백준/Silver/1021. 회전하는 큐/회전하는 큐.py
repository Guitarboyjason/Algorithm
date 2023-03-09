# 1. 첫 번째 원소를 뽑는다.
# 2. 왼쪽으로 한칸 이동시킨다. (shift - left)
# 3. 오른쪽으로 한칸 이동시킨다. (right - shift)

# 배열의 처음을 뽑는다면 나머지를 -1씩 해준다.
# 처음보다 큰 수라면 left로 이동 모든 수를 -1씩
# 총 남은 갯수가 N이라고 할 때 뽑을 때 마다 -1씩
# 처음보다 큰수긴 한데 N//2 보다 크면 오른쪽
# 그러면 모든 수를 +1씩
from collections import deque
N, M = map(int, input().split())

want_list = deque(map(int, input().split()))
cnt = 0
num_list = deque(i for i in range(1, N+1))
# print(num_list)
while want_list:
    wants = want_list.popleft()
    if num_list[0] == wants:
        num_list.popleft()
        continue
    if num_list.index(wants) > len(num_list) // 2:
        cnt += len(num_list) - num_list.index(wants)
        for i in range(num_list.index(wants)):
            num_list.append(num_list.popleft())
        num_list.popleft()
    else:
        cnt += num_list.index(wants)
        for i in range(num_list.index(wants)):
            num_list.append(num_list.popleft())
        num_list.popleft()
print(cnt)
# now = 1
# while want_list:
#     node = want_list.popleft()
#     if node == now:
#         now += 1
#         N -= 1
#         continue
#     elif abs(node - N) > N - abs(node - now):
#         cnt += N-abs(node-now)
#         now = node
#         N -= 1
#     else:
#         cnt += abs(node-N)
#         now = node
#         N -= 1
# print(cnt)
