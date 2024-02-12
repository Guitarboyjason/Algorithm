# """
# ID, 문제 번호, 점수
# 최고 점수가 해당 문제의 최종 점수
# 한번도 제출하지 않으면 최종 점수는 0
# 각 문제 점수의 총합
# 나의 순위 : 나보다 높은 점수의 팀 수 +1
# 점수가 동일 할 시,
# 최종점수가 같은 경우 : 풀이를 제출한 횟수가 적은 팀이 더 높음
# 제출 횟수도 같은 경우, 마지막 제출 시간이 빠른 팀
# """

# import sys

# input = sys.stdin.readline

# from collections import deque


# for T in range(int(input())):
#     nums_team, nums_problem, team_id, nums_log = map(int, input().split())

#     submit_list = deque()
#     score_dict = {
#         i: {j: 0 for j in range(1, nums_problem + 1)} for i in range(1, nums_team + 1)
#     }
#     submit_cnt = {i: 0 for i in range(1, nums_team + 1)}
#     for _ in range(nums_log):
#         id, problem, score = map(int, input().split())
#         if id in submit_list:
#             submit_list.remove(id)
#         submit_list.append(id)
#         submit_cnt[id] += 1
#         score_dict[id][problem] = max(score_dict[id][problem], score)
#     final_grade = 1

#     final_score_dict = {i[0]: sum(i[1].values()) for i in score_dict.items()}

#     my_team_score = final_score_dict[team_id]

#     final_grade += len([i for i in final_score_dict.items() if i[1] > my_team_score])

#     same_score_teams_list = [
#         i[0]
#         for i in final_score_dict.items()
#         if i[0] != team_id and i[1] == my_team_score
#     ]

#     for t in same_score_teams_list.copy():
#         if submit_cnt[t] < submit_cnt[team_id]:
#             final_grade += 1
#             same_score_teams_list.remove(t)
#         elif submit_cnt[t] > submit_cnt[team_id]:
#             same_score_teams_list.remove(t)

#     compare_list = [
#         i for idx, i in enumerate(submit_list) if idx < submit_list.index(id)
#     ]
#     for t in same_score_teams_list:
#         if t in compare_list:
#             final_grade += 1
#     print(final_grade)
#     # my_team_last_submit =
#     # submit_compare_list = []


import sys

input = sys.stdin.readline

from collections import deque


for T in range(int(input())):
    nums_team, nums_problem, team_id, nums_log = map(int, input().split())

    submit_list = deque()
    score_dict = {
        i: {j: 0 for j in range(nums_problem + 2)}
        for i in range(1, nums_team + 1)  # 0번째는 submit_cnt 횟수로 하자 마지막은 last_submit
    }

    for i in range(nums_log):
        id, problem, score = map(int, input().split())
        score_dict[id][0] += 1
        score_dict[id][problem] = max(score_dict[id][problem], score)
        score_dict[id][nums_problem + 1] = i

    my_team_score = sum(list(score_dict[team_id].values())[1:-1])
    # 저장 : 팀 id, Team score, submit_cnt , last_submit
    compare_list = [
        [
            i,
            sum(list(score_dict[i].values())[1:-1]),
            score_dict[i][0],
            score_dict[i][nums_problem + 1],
        ]
        for i in score_dict
        if sum(list(score_dict[i].values())[1:-1]) >= my_team_score
    ]
    compare_list.sort(key=lambda x: x[3])
    compare_list.sort(key=lambda x: x[2])
    compare_list.sort(key=lambda x: x[1], reverse=True)

    cnt = 1
    for i in compare_list:
        if i[0] == team_id:
            break
        else:
            cnt += 1
    print(cnt)
