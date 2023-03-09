

S = input()
answer = ""
tmp = ""
flag = False
for i in S:
    if i == "<" or i != ">" and flag:
        if i == "<":
            answer += tmp[::-1]
            tmp = ""
        tmp += i
        flag = True

        continue
    if i == ">":
        tmp += i
        flag = False
        answer += tmp
        tmp = ""
        continue
    if i == " ":
        answer += tmp[::-1] + " "

        tmp = ""
        continue
    tmp += i
if tmp:
    answer += tmp[::-1]

# commands = list(map(str, S.split()))
# for i in commands:
#     if i[0] == "<" or i[-1] == ">":
#         answer += i
#     else:
#         answer += i[::-1]
#     answer += " "
print(answer)
