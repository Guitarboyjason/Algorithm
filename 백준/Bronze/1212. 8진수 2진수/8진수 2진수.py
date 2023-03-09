transport = {"0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
num = input()
if num == "0":
    print("0")
else:
    for i in transport:
        num = num.replace(i,transport[i])
    print(num.lstrip("0"))