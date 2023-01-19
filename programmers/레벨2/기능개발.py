from collections import deque

def solution(progresses,speeds):
    answer = []
    cnt = 0
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        now = progresses.popleft()
        time = speeds.popleft()
        while now < 100:
            now += time
            cnt += 1
        answer.append(1)
        next = 0
        while next < len(progresses) and progresses[next] + speeds[next] * cnt >= 100:
            progresses.popleft()
            speeds.popleft()
            answer[-1] += 1
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1,1,1,1,1,1]

print(solution(progresses,speeds))
