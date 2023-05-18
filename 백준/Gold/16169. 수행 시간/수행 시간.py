"""
모든 컴퓨터는 1번부터 n번까지 번호가 매겨져 있다. 모든 컴퓨터는 각자의 계급과 동작 속도를 가지고 있다. 또한 계급과 동작 속도는 모두 양의 정수이다.
i번 컴퓨터와 j번 컴퓨터 간의 전송 시간은 (i - j)^2이다.
각 n개의 컴퓨터의 계급은 c1, c2, … cn이다. (1 ≤ c1 ≤ c2 ≤ … ≤ cn ≤ n). 주어진 컴퓨터의 계급을 오름차순으로 정렬했을 경우, | cj -cj-1 |≤ 1이다. 
제일 낮은 계급의 컴퓨터를 제외한 모든 컴퓨터들은 자신보다 한 단계 낮은 계급의 모든 컴퓨터에게 정보를 전달받아야만 동작을 시작 할 수 있다. 이 때, 동작을 시작하기 위해서는 그 컴퓨터의 동작 속도만큼의 시간이 소요된다.
제일 낮은 계급의 컴퓨터는 전달 받을 정보가 없다. 따라서 시스템 시동과 동시에 동작한다.
계급이 c인 컴퓨터가 동작을 마치면 c+1의 계급을 가진 모든 컴퓨터에 정보를 전달 후 종료된다.
모든 컴퓨터가 동작을 마치고 종료되면 이 시스템의 임무 수행이 끝난다.
가장 낮은 계급은 1이다.
"""
"""
9
1 1
3 9
3 1
4 2
4 2
2 5
1 30
4 2
5 3
"""
# 연속되는 계급의 차가 2보다 클 수 없다.
# 전체 임무 수행이 다 끝날 때가 언제냐
# 최소라 말하지 않았으므로 그냥 끝날때를 찾으면 될 것 같은데
# 아 자신보다 낮으ㅡㄴ 계급의 모든 컴퓨터의 정보를 전달 받아야 하는구나
import sys

input = sys.stdin.readline


def work():
    for level in range(1, n + 1):
        for start, node_num, time in graph[level]:
            # done_time[level].append(start + time)  # 굳이?
            if level != max_level:
                for next in graph[level + 1]:
                    next[0] = max(
                        next[0], start + time + (node_num - next[1]) ** 2
                    )  # 마지막에 저장되는 친구를 확인하면 전체 실행 시간이 나올듯


n = int(input())
graph = {level: [] for level in range(1, n + 1)}

max_level = 0
for i in range(1, n + 1):
    level, t = map(int, input().split())
    graph[level].append([0, i, t])  # 시작시간, 노드 번호, 동작시간, (i-j)^2를 구하기 위해
    if max_level < level:
        max_level = level
    # 시작시간은 max로 계속 갱신해야 할 것

for i in graph[1]:
    i[0] = 0
# done_time = {i: [] for i in range(1, n + 1)}


# 각 레벨별로 끝나는 시간은 max(level)일거고,
# 그럼 끝나는 시간은 동일하지만 각 j별로 시작하는 시간은 다를 것이다.
# max(level)이라고 해서 걔가 가장 마지막에 들어오지 않을 수도 있다.


work()
# from pprint import pprint

# pprint(graph)
print(max([sum([i[0], i[2]]) for i in graph[max_level]]))
