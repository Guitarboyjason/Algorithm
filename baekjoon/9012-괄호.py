# def find_VPS(string,cnt):
#     if string[0] == '(':
#         find_VPS(string[1:],cnt+1)
#     else:
#         return cnt-1        #return값이 -1이면 )가 하나 더 들어간 것
#
#
# T = int(input())
# for _ in range(T):
#     string = input()
#     if find_VPS(string,0) == 0:
#         print("YES")
#     else:
#         print("NO")
#
#


# #반 나눠서 대칭을 이루면 yes, 아니면 no
#
# def find_VPS(string):
#     half = string[:int(len(string)/2)+1]
#     compare = string[int(len(string)/2)+1:]
#     for i in range(len(compare)):
#         if compare[i] == '(':
#             compare = compare[:i] + ')' + compare[i+1:]
#         else:
#             compare = compare[:i] + '(' + compare[i+1:]
#
#     if half == compare:
#         print("YES")
#     else:
#         print("NO")
# T = int(input())
# for _ in range(T):
#     string = input()
#     find_VPS(string)
