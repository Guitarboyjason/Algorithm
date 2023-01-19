# import math
# #기본 시간 : 기본 요금 : 단위 시간 : 단위 요금
#
# # 스택으로 구현하면 편하겠다.
# # 아니면 딕셔너리로 구현해도 될 듯
#
# def time_calculator(in_time,out_time):
#     hour ,min = out_time.split(":")
#     time = int(hour)*60 + int(min)
#     hour ,min = in_time.split(":")
#     time -= int(hour)*60 + int(min)
#     return time
#
# def cost_calculator(fees,time):
#     if time <= fees[0]:
#         return fees[1]
#     else:
#         time -= fees[0]
#         time /= fees[2]
#         return fees[0] +  math.ceil(time)*fees[3]
#
# def solution(fees,records):
#     arr = dict()
#     answer = []
#     answer = dict()
#     for i in records:
#         time,number,direction = i.split()
#         if direction == "IN":
#             arr[number] = [time,number]
#         else:
#
#             #answer.append([number,cost_calculator(fees,time_calculator(arr[number][0],time))])
#             # if answer[number] == n
#             if number in answer:
#                 answer[number] +=cost_calculator(fees,time_calculator(arr[number][0],time))
#             else:
#                 answer[number]=cost_calculator(fees,time_calculator(arr[number][0],time))
#             arr.pop(number)
#     while arr:
#         tmp = arr.popitem()
#         print(tmp)
#         # answer.append([tmp[0],cost_calculator(fees,time_calculator(tmp[1][0],"23:59"))])
#         if tmp[0] in answer:
#                 answer[tmp[0]] +=cost_calculator(fees,time_calculator(tmp[1][0],"23:59"))
#         else:
#             answer[tmp[0]]=cost_calculator(fees,time_calculator(tmp[1][0],"23:59"))
#     # answer.sort(key=lambda x : x[0])
#     return answer
#
# fees = [180,5000,10,600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
#
# a = dict()
# # print(a[0])
# print(solution(fees,records))


import math
#기본 시간 : 기본 요금 : 단위 시간 : 단위 요금

# 스택으로 구현하면 편하겠다.
# 아니면 딕셔너리로 구현해도 될 듯

def time_calculator(in_time,out_time):
    hour ,min = out_time.split(":")
    time = int(hour)*60 + int(min)
    hour ,min = in_time.split(":")
    time -= int(hour)*60 + int(min)
    return time

def cost_calculator(fees,time):
    if time <= fees[0]:#기본시간
        return fees[1]#기본요금
    else:
        time -= fees[0]#기본시간
        time /= fees[2]#단위시간
        return fees[1] +  math.ceil(time)*fees[3]

def solution(fees,records):
    arr = dict()
    answer = []
    answer = dict()
    real_answer = []
    for i in records:
        time,number,direction = i.split()
        if direction == "IN":
            arr[number] = [time,number]
        else:

            #answer.append([number,cost_calculator(fees,time_calculator(arr[number][0],time))])
            # if answer[number] == n
            if number in answer:
                answer[number] +=time_calculator(arr[number][0],time)
            else:
                answer[number]=time_calculator(arr[number][0],time)
            arr.pop(number)
    while arr:
        tmp = arr.popitem()
        # answer.append([tmp[0],cost_calculator(fees,time_calculator(tmp[1][0],"23:59"))])
        if tmp[0] in answer:
                answer[tmp[0]] +=time_calculator(tmp[1][0],"23:59")
        else:
            answer[tmp[0]]=time_calculator(tmp[1][0],"23:59")
    for i in answer:
        real_answer.append([i,cost_calculator(fees,answer[i])])
    real_answer.sort(key=lambda x:x[0])
    answer = []
    for i in real_answer:
        answer.append(i[1])
    return answer

fees = [180,5000,10,600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

a = dict()
# print(a[0])
print(solution(fees,records))
