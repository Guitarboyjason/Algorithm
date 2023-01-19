dict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

T = int(input())
for test_case in range(1,T+1):
    date = input()
    # year = ""
    # month = ""
    # day = ""
    # for i in range(len(date)):
    #     if i < 4:
    #         year += date[i]
    #     elif i < 6:
    #         month += date[i]
    #     else:
    #         day += date[i]
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    if int(month) > 12 or int(month) < 1:
        answer = "-1"
    elif dict[int(month)] >= int(day) and int(day) >= 1:
        answer = f"{year}/{month}/{day}"
    else:
        answer = "-1"

    print(f"#{test_case} {answer}")
# print(dict)
# print(dict[2])
# print(int("02"))
# print(dict[int("02")])
