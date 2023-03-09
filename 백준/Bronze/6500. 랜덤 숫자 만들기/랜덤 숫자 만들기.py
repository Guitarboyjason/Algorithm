

n = 4

finished = False
num = int(input())
if num == 0:
    finished = True
while not finished:

    tmp = []
    while len(str(num))<4:
        num = '0'+str(num)
    while num not in tmp:
        tmp.append(str(num))
        num = str(int(num)**2)
        while len(num) < 2*n:
            num = '0'+num
        num = num[2:6]
    print(len(tmp))
    num = int(input())
    if num == 0:
        finished = True
