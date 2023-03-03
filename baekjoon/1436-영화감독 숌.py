# N = int(input())
# list_6 = []
# for i in range(3000):
#     tmp = list(str(i))
#     # print(tmp)
#     # print(list_6)
#     for j in range(len(tmp)+1):
#         # print(tmp[:j],tmp[j:])
#         list_6.append(int("".join("".join(tmp[:j])+"666"+"".join(tmp[j:]))))
# # print(len(list_6))
# list_6 = list(set(list_6))
# list_6.sort()
# # print(len(list_6)[N])
# print(list_6[N-1])

N = int(input())
list_666 =[]
for i in range(666,1000000):
    if "666" in str(i):
        list_666.append(i)
print(list_666[N-1])