n = int(input())

charge_arr = [500,100,50,10,5,1]

charge = 1000-n
count = 0
while charge != 0:
    for i in charge_arr:
        if charge >= i:
            count += 1
            charge -= i
            break
print(count)
