# # num = input()
# # number_10 = 0
# # # print(reversed(num))
# # num = num[::-1]
# # for i in range(len(num)):
# #     number_10 += int(8**i * int(num[i]))
# # # print(number_10)
# # num = input()
# # print(int(num))
# # print("{:b}".format(int(num)))
# # print("{:o}".format(number_10))
# # num = "16"
# # print(bin(int(oct(int(input()))[2:]))[2:])
# print(oct(int(input())))
# # num = bin(oct(int(input())))

# # print(num)
# # print(num)
# # print(oct(int(input())))
# # print("{:b}".format(num))


transport = {"0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
num = input()
if num == "0":
    print("0")
else:
    # print(transport)
    for i in transport:
        # print(i)
        num = num.replace(i,transport[i])

    print(num.lstrip("0"))